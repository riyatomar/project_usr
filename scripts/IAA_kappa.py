import sys
import re
from sklearn.metrics import cohen_kappa_score

# Column names mapping
COLUMN_NAMES = {
    0: "concept",
    1: "index",
    2: "sem-cat",
    3: "morpho-sem",
    4: "dependency",
    5: "discourse",
    6: "spk-view",
    7: "scope",
    8: "cxn"
}

def parse_file(filename):
    segments = {}
    current_segment = None
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("<segment_id="):
                current_segment = re.findall(r"<segment_id=([^>]+)>", line)[0]
                segments[current_segment] = {}
            elif line.startswith("</segment_id>"):
                current_segment = None
            elif line.startswith("#") or line.startswith("%"):
                continue
            elif current_segment:
                parts = line.split("\t")
                if parts:
                    key = parts[0]
                    segments[current_segment][key] = parts
    return segments

def calculate_iaa(segments1, segments2):
    results = {}
    disagreements = []
    common_segments = set(segments1.keys()) & set(segments2.keys())

    for seg in common_segments:
        rows1 = segments1[seg]
        rows2 = segments2[seg]
        common_keys = set(rows1.keys()) & set(rows2.keys())
        if not common_keys:
            continue

        ncols = min(
            min(len(rows1[k]) for k in common_keys),
            min(len(rows2[k]) for k in common_keys)
        )

        for col in range(ncols):
            col_data1 = [rows1[k][col] for k in common_keys]
            col_data2 = [rows2[k][col] for k in common_keys]

            if all(v == "-" for v in col_data1 + col_data2):
                continue

            # Track per-cell disagreements
            for k in common_keys:
                v1, v2 = rows1[k][col], rows2[k][col]
                if v1 != v2:
                    disagreements.append({
                        "segment": seg,
                        "row": k,
                        "column": COLUMN_NAMES.get(col, f"Column {col}"),
                        "annotator1": v1,
                        "annotator2": v2
                    })

            agreement = sum(1 for a, b in zip(col_data1, col_data2) if a == b) / len(col_data1)

            combined_labels = set(col_data1 + col_data2)
            if len(combined_labels) == 1:
                kappa = 1.0 if agreement == 1.0 else 0.0
            else:
                kappa = cohen_kappa_score(col_data1, col_data2)

            results.setdefault(col, []).append((kappa, agreement))

    final_results = {
        col: {
            "kappa": sum(v[0] for v in vals) / len(vals),
            "agreement": sum(v[1] for v in vals) / len(vals)
        }
        for col, vals in results.items()
    }
    return final_results, disagreements

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python iaa_calc.py file1 file2")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]
    segments1 = parse_file(file1)
    segments2 = parse_file(file2)

    iaa_results, disagreements = calculate_iaa(segments1, segments2)

    print("IAA results per column:")
    for col, metrics in iaa_results.items():
        name = COLUMN_NAMES.get(col, f"Column {col}")
        print(f"{name}: Kappa={metrics['kappa']:.4f}, Agreement={metrics['agreement']*100:.2f}%")

    print("\nTop 20 disagreements:")
    for d in disagreements[:40]:
        print(f"Segment {d['segment']}, Row {d['row']}, Column {d['column']} → "
              f"A1: {d['annotator1']} | A2: {d['annotator2']}")

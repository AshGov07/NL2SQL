import json
from statistics import mean


class BenchmarkProfiler:

    def __init__(self, model_name):

        self.model_name = model_name
        self.records = []

    def add_record(
        self,
        question,
        llm_time,
        extract_time,
        validation_time,
        repair_time,
        total_time,
        status
    ):

        self.records.append(
            {
                "question": question,
                "model": self.model_name,
                "llm_time": round(llm_time, 4),
                "extract_time": round(extract_time, 4),
                "validation_time": round(
                    validation_time,
                    4
                ),
                "repair_time": round(
                    repair_time,
                    4
                ),
                "total_time": round(
                    total_time,
                    4
                ),
                "status": status
            }
        )

    def print_summary(self):

        if not self.records:
            return

        print("\n")
        print("=" * 80)
        print("MODEL PERFORMANCE")
        print("=" * 80)

        print(
            f"Model: {self.model_name}"
        )

        print(
            f"Avg LLM Time: "
            f"{mean(r['llm_time'] for r in self.records):.2f} sec"
        )

        print(
            f"Avg Extraction Time: "
            f"{mean(r['extract_time'] for r in self.records):.4f} sec"
        )

        print(
            f"Avg Validation Time: "
            f"{mean(r['validation_time'] for r in self.records):.4f} sec"
        )

        print(
            f"Avg Repair Time: "
            f"{mean(r['repair_time'] for r in self.records):.4f} sec"
        )

        print(
            f"Avg Total Time: "
            f"{mean(r['total_time'] for r in self.records):.2f} sec"
        )

    def save(self):

        filename = (
            "performance_"
            + self.model_name.replace(
                ":",
                "_"
            )
            + ".json"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.records,
                f,
                indent=4
            )

        print(
            f"\nSaved performance report: {filename}"
        )
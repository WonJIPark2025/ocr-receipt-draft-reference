try:
    from dotenv import load_dotenv
    load_dotenv()
except ModuleNotFoundError as e:
    raise RuntimeError(
        "Full pipeline requires optional dependencies. "
        "Please install python-dotenv and configure environment variables."
    ) from e

from src.legacy.full_pipeline import run_pipeline, run_receipt_pipeline

def main():
    parsed = run_pipeline("data/raw/sample_receipt.jpg")
    receipt = run_receipt_pipeline(parsed)

    print(receipt["validation"])

if __name__ == "__main__":
    main()

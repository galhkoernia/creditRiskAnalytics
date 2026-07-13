from config.settings import (
    PROCESSED_DATASET
)

from utils.data_loader import (
    load_dataset
)

from services.eda_service import (
    run_complete_eda
)


def main():

    print("=" * 60)
    print("FinanKu Credit Risk Analysis")
    print("=" * 60)

    df = load_dataset(
        PROCESSED_DATASET
    )

    results = run_complete_eda(
        df
    )

    print("\nEDA completed successfully.")

    return results


if __name__ == "__main__":
    main()
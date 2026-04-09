from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def load_data():
    """
    Self-contained sample data so the script runs independently.
    """
    data = {
        "month": [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ],
        "revenue_jod": [
            18200, 19500, 20100, 21400, 22800, 23600,
            24900, 26100, 27800, 29100, 30700, 32500
        ]
    }
    return pd.DataFrame(data)


def create_chart(df):
    output_path = Path(__file__).resolve().parent / "chart.png"

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        df["month"],
        df["revenue_jod"],
        marker="o",
        linewidth=2.5
    )

    ax.set_title(
        "Monthly Revenue Rose Consistently Across the Year in Amman Digital Market",
        fontsize=14,
        pad=16
    )
    ax.set_xlabel("Month", fontsize=11)
    ax.set_ylabel("Revenue (JOD)", fontsize=11)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle="--", alpha=0.35)

    first_row = df.iloc[0]
    last_row = df.iloc[-1]
    peak_row = df.loc[df["revenue_jod"].idxmax()]

    ax.annotate(
        f"Start: {first_row['revenue_jod']:,} JOD",
        xy=(first_row["month"], first_row["revenue_jod"]),
        xytext=(0, 15),
        textcoords="offset points",
        ha="center",
        fontsize=9
    )

    ax.annotate(
        f"Peak: {peak_row['revenue_jod']:,} JOD",
        xy=(peak_row["month"], peak_row["revenue_jod"]),
        xytext=(0, 15),
        textcoords="offset points",
        ha="center",
        fontsize=9
    )

    growth_pct = ((last_row["revenue_jod"] - first_row["revenue_jod"]) / first_row["revenue_jod"]) * 100

    fig.text(
        0.12,
        0.01,
        f"Insight: revenue increased by {growth_pct:.1f}% from January to December, indicating steady business growth.",
        fontsize=9
    )

    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main():
    df = load_data()
    create_chart(df)
    print("chart.png created successfully.")


if __name__ == "__main__":
    main()
#
# Created on Mon Jul 13 2026
#
# Copyright (c) 2026 galhkoernia
#

TARGET_COLUMN = "Unpaid Tagging"

ID_COLUMN = "Customer ID"

CATEGORICAL_COLUMNS = [
    "City",
    "Branch Code"
]

NUMERICAL_COLUMNS = [
    "Age",
    "Avg. Annual Income/Month",
    "Avg Balance",
    "Balance Change",
    "Avg Products",
    "Activity Rate"
]

FEATURE_COLUMNS = [
    "Age",
    "Avg. Annual Income/Month",
    "City",
    "Branch Code",
    "Avg Balance",
    "Balance Change",
    "Avg Products",
    "Activity Rate"
]

UNIVARIATE_ANALYSIS_COLUMNS = {
    "credit_risk": [
        TARGET_COLUMN
    ],
    "customer_profile": [
        "Age",
        "Avg. Annual Income/Month"
    ],
    "geographic": [
        "City"
    ],
    "financial": [
        "Avg Balance"
    ],
    "product": [
        "Avg Products"
    ],
    "activity": [
        "Activity Rate"
    ]
}

CORRELATION_COLUMNS = [
    "Age",
    "Avg. Annual Income/Month",
    "Avg Balance",
    "Balance Change",
    "Avg Products",
    "Activity Rate",
    TARGET_COLUMN
]
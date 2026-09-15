"""
Pytest suite for Finance, Billing & Payroll
"""
import pytest
from app.domains.finance.schemas import *

def test_finance_entity_1_schema_validation():
    obj = FinanceSchemaEntity1Create(
        entity_code="TEST_FINANCE_1",
        name="Test Entity 1",
        value_amount=1 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_1"
    assert obj.value_amount == 1 * 100.5

def test_finance_entity_2_schema_validation():
    obj = FinanceSchemaEntity2Create(
        entity_code="TEST_FINANCE_2",
        name="Test Entity 2",
        value_amount=2 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_2"
    assert obj.value_amount == 2 * 100.5

def test_finance_entity_3_schema_validation():
    obj = FinanceSchemaEntity3Create(
        entity_code="TEST_FINANCE_3",
        name="Test Entity 3",
        value_amount=3 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_3"
    assert obj.value_amount == 3 * 100.5

def test_finance_entity_4_schema_validation():
    obj = FinanceSchemaEntity4Create(
        entity_code="TEST_FINANCE_4",
        name="Test Entity 4",
        value_amount=4 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_4"
    assert obj.value_amount == 4 * 100.5

def test_finance_entity_5_schema_validation():
    obj = FinanceSchemaEntity5Create(
        entity_code="TEST_FINANCE_5",
        name="Test Entity 5",
        value_amount=5 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_5"
    assert obj.value_amount == 5 * 100.5

def test_finance_entity_6_schema_validation():
    obj = FinanceSchemaEntity6Create(
        entity_code="TEST_FINANCE_6",
        name="Test Entity 6",
        value_amount=6 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_6"
    assert obj.value_amount == 6 * 100.5

def test_finance_entity_7_schema_validation():
    obj = FinanceSchemaEntity7Create(
        entity_code="TEST_FINANCE_7",
        name="Test Entity 7",
        value_amount=7 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_7"
    assert obj.value_amount == 7 * 100.5

def test_finance_entity_8_schema_validation():
    obj = FinanceSchemaEntity8Create(
        entity_code="TEST_FINANCE_8",
        name="Test Entity 8",
        value_amount=8 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_8"
    assert obj.value_amount == 8 * 100.5

def test_finance_entity_9_schema_validation():
    obj = FinanceSchemaEntity9Create(
        entity_code="TEST_FINANCE_9",
        name="Test Entity 9",
        value_amount=9 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_9"
    assert obj.value_amount == 9 * 100.5

def test_finance_entity_10_schema_validation():
    obj = FinanceSchemaEntity10Create(
        entity_code="TEST_FINANCE_10",
        name="Test Entity 10",
        value_amount=10 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_10"
    assert obj.value_amount == 10 * 100.5

def test_finance_entity_11_schema_validation():
    obj = FinanceSchemaEntity11Create(
        entity_code="TEST_FINANCE_11",
        name="Test Entity 11",
        value_amount=11 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_11"
    assert obj.value_amount == 11 * 100.5

def test_finance_entity_12_schema_validation():
    obj = FinanceSchemaEntity12Create(
        entity_code="TEST_FINANCE_12",
        name="Test Entity 12",
        value_amount=12 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_12"
    assert obj.value_amount == 12 * 100.5

def test_finance_entity_13_schema_validation():
    obj = FinanceSchemaEntity13Create(
        entity_code="TEST_FINANCE_13",
        name="Test Entity 13",
        value_amount=13 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_13"
    assert obj.value_amount == 13 * 100.5

def test_finance_entity_14_schema_validation():
    obj = FinanceSchemaEntity14Create(
        entity_code="TEST_FINANCE_14",
        name="Test Entity 14",
        value_amount=14 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_14"
    assert obj.value_amount == 14 * 100.5

def test_finance_entity_15_schema_validation():
    obj = FinanceSchemaEntity15Create(
        entity_code="TEST_FINANCE_15",
        name="Test Entity 15",
        value_amount=15 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_15"
    assert obj.value_amount == 15 * 100.5

def test_finance_entity_16_schema_validation():
    obj = FinanceSchemaEntity16Create(
        entity_code="TEST_FINANCE_16",
        name="Test Entity 16",
        value_amount=16 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_16"
    assert obj.value_amount == 16 * 100.5

def test_finance_entity_17_schema_validation():
    obj = FinanceSchemaEntity17Create(
        entity_code="TEST_FINANCE_17",
        name="Test Entity 17",
        value_amount=17 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_17"
    assert obj.value_amount == 17 * 100.5

def test_finance_entity_18_schema_validation():
    obj = FinanceSchemaEntity18Create(
        entity_code="TEST_FINANCE_18",
        name="Test Entity 18",
        value_amount=18 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_18"
    assert obj.value_amount == 18 * 100.5

def test_finance_entity_19_schema_validation():
    obj = FinanceSchemaEntity19Create(
        entity_code="TEST_FINANCE_19",
        name="Test Entity 19",
        value_amount=19 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_19"
    assert obj.value_amount == 19 * 100.5

def test_finance_entity_20_schema_validation():
    obj = FinanceSchemaEntity20Create(
        entity_code="TEST_FINANCE_20",
        name="Test Entity 20",
        value_amount=20 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_20"
    assert obj.value_amount == 20 * 100.5

def test_finance_entity_21_schema_validation():
    obj = FinanceSchemaEntity21Create(
        entity_code="TEST_FINANCE_21",
        name="Test Entity 21",
        value_amount=21 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_21"
    assert obj.value_amount == 21 * 100.5

def test_finance_entity_22_schema_validation():
    obj = FinanceSchemaEntity22Create(
        entity_code="TEST_FINANCE_22",
        name="Test Entity 22",
        value_amount=22 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_22"
    assert obj.value_amount == 22 * 100.5

def test_finance_entity_23_schema_validation():
    obj = FinanceSchemaEntity23Create(
        entity_code="TEST_FINANCE_23",
        name="Test Entity 23",
        value_amount=23 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_23"
    assert obj.value_amount == 23 * 100.5

def test_finance_entity_24_schema_validation():
    obj = FinanceSchemaEntity24Create(
        entity_code="TEST_FINANCE_24",
        name="Test Entity 24",
        value_amount=24 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_24"
    assert obj.value_amount == 24 * 100.5

def test_finance_entity_25_schema_validation():
    obj = FinanceSchemaEntity25Create(
        entity_code="TEST_FINANCE_25",
        name="Test Entity 25",
        value_amount=25 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_25"
    assert obj.value_amount == 25 * 100.5

def test_finance_entity_26_schema_validation():
    obj = FinanceSchemaEntity26Create(
        entity_code="TEST_FINANCE_26",
        name="Test Entity 26",
        value_amount=26 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_26"
    assert obj.value_amount == 26 * 100.5

def test_finance_entity_27_schema_validation():
    obj = FinanceSchemaEntity27Create(
        entity_code="TEST_FINANCE_27",
        name="Test Entity 27",
        value_amount=27 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_27"
    assert obj.value_amount == 27 * 100.5

def test_finance_entity_28_schema_validation():
    obj = FinanceSchemaEntity28Create(
        entity_code="TEST_FINANCE_28",
        name="Test Entity 28",
        value_amount=28 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_28"
    assert obj.value_amount == 28 * 100.5

def test_finance_entity_29_schema_validation():
    obj = FinanceSchemaEntity29Create(
        entity_code="TEST_FINANCE_29",
        name="Test Entity 29",
        value_amount=29 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_29"
    assert obj.value_amount == 29 * 100.5

def test_finance_entity_30_schema_validation():
    obj = FinanceSchemaEntity30Create(
        entity_code="TEST_FINANCE_30",
        name="Test Entity 30",
        value_amount=30 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_30"
    assert obj.value_amount == 30 * 100.5

def test_finance_entity_31_schema_validation():
    obj = FinanceSchemaEntity31Create(
        entity_code="TEST_FINANCE_31",
        name="Test Entity 31",
        value_amount=31 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_31"
    assert obj.value_amount == 31 * 100.5

def test_finance_entity_32_schema_validation():
    obj = FinanceSchemaEntity32Create(
        entity_code="TEST_FINANCE_32",
        name="Test Entity 32",
        value_amount=32 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_32"
    assert obj.value_amount == 32 * 100.5

def test_finance_entity_33_schema_validation():
    obj = FinanceSchemaEntity33Create(
        entity_code="TEST_FINANCE_33",
        name="Test Entity 33",
        value_amount=33 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_33"
    assert obj.value_amount == 33 * 100.5

def test_finance_entity_34_schema_validation():
    obj = FinanceSchemaEntity34Create(
        entity_code="TEST_FINANCE_34",
        name="Test Entity 34",
        value_amount=34 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_34"
    assert obj.value_amount == 34 * 100.5

def test_finance_entity_35_schema_validation():
    obj = FinanceSchemaEntity35Create(
        entity_code="TEST_FINANCE_35",
        name="Test Entity 35",
        value_amount=35 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_35"
    assert obj.value_amount == 35 * 100.5

def test_finance_entity_36_schema_validation():
    obj = FinanceSchemaEntity36Create(
        entity_code="TEST_FINANCE_36",
        name="Test Entity 36",
        value_amount=36 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_36"
    assert obj.value_amount == 36 * 100.5

def test_finance_entity_37_schema_validation():
    obj = FinanceSchemaEntity37Create(
        entity_code="TEST_FINANCE_37",
        name="Test Entity 37",
        value_amount=37 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_37"
    assert obj.value_amount == 37 * 100.5

def test_finance_entity_38_schema_validation():
    obj = FinanceSchemaEntity38Create(
        entity_code="TEST_FINANCE_38",
        name="Test Entity 38",
        value_amount=38 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_38"
    assert obj.value_amount == 38 * 100.5

def test_finance_entity_39_schema_validation():
    obj = FinanceSchemaEntity39Create(
        entity_code="TEST_FINANCE_39",
        name="Test Entity 39",
        value_amount=39 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_39"
    assert obj.value_amount == 39 * 100.5

def test_finance_entity_40_schema_validation():
    obj = FinanceSchemaEntity40Create(
        entity_code="TEST_FINANCE_40",
        name="Test Entity 40",
        value_amount=40 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_40"
    assert obj.value_amount == 40 * 100.5

def test_finance_entity_41_schema_validation():
    obj = FinanceSchemaEntity41Create(
        entity_code="TEST_FINANCE_41",
        name="Test Entity 41",
        value_amount=41 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_41"
    assert obj.value_amount == 41 * 100.5

def test_finance_entity_42_schema_validation():
    obj = FinanceSchemaEntity42Create(
        entity_code="TEST_FINANCE_42",
        name="Test Entity 42",
        value_amount=42 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_42"
    assert obj.value_amount == 42 * 100.5

def test_finance_entity_43_schema_validation():
    obj = FinanceSchemaEntity43Create(
        entity_code="TEST_FINANCE_43",
        name="Test Entity 43",
        value_amount=43 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_43"
    assert obj.value_amount == 43 * 100.5

def test_finance_entity_44_schema_validation():
    obj = FinanceSchemaEntity44Create(
        entity_code="TEST_FINANCE_44",
        name="Test Entity 44",
        value_amount=44 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_44"
    assert obj.value_amount == 44 * 100.5

def test_finance_entity_45_schema_validation():
    obj = FinanceSchemaEntity45Create(
        entity_code="TEST_FINANCE_45",
        name="Test Entity 45",
        value_amount=45 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_45"
    assert obj.value_amount == 45 * 100.5

def test_finance_entity_46_schema_validation():
    obj = FinanceSchemaEntity46Create(
        entity_code="TEST_FINANCE_46",
        name="Test Entity 46",
        value_amount=46 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_46"
    assert obj.value_amount == 46 * 100.5

def test_finance_entity_47_schema_validation():
    obj = FinanceSchemaEntity47Create(
        entity_code="TEST_FINANCE_47",
        name="Test Entity 47",
        value_amount=47 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_47"
    assert obj.value_amount == 47 * 100.5

def test_finance_entity_48_schema_validation():
    obj = FinanceSchemaEntity48Create(
        entity_code="TEST_FINANCE_48",
        name="Test Entity 48",
        value_amount=48 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_48"
    assert obj.value_amount == 48 * 100.5

def test_finance_entity_49_schema_validation():
    obj = FinanceSchemaEntity49Create(
        entity_code="TEST_FINANCE_49",
        name="Test Entity 49",
        value_amount=49 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_49"
    assert obj.value_amount == 49 * 100.5

def test_finance_entity_50_schema_validation():
    obj = FinanceSchemaEntity50Create(
        entity_code="TEST_FINANCE_50",
        name="Test Entity 50",
        value_amount=50 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_50"
    assert obj.value_amount == 50 * 100.5

def test_finance_entity_51_schema_validation():
    obj = FinanceSchemaEntity51Create(
        entity_code="TEST_FINANCE_51",
        name="Test Entity 51",
        value_amount=51 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_51"
    assert obj.value_amount == 51 * 100.5

def test_finance_entity_52_schema_validation():
    obj = FinanceSchemaEntity52Create(
        entity_code="TEST_FINANCE_52",
        name="Test Entity 52",
        value_amount=52 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_52"
    assert obj.value_amount == 52 * 100.5

def test_finance_entity_53_schema_validation():
    obj = FinanceSchemaEntity53Create(
        entity_code="TEST_FINANCE_53",
        name="Test Entity 53",
        value_amount=53 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_53"
    assert obj.value_amount == 53 * 100.5

def test_finance_entity_54_schema_validation():
    obj = FinanceSchemaEntity54Create(
        entity_code="TEST_FINANCE_54",
        name="Test Entity 54",
        value_amount=54 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_54"
    assert obj.value_amount == 54 * 100.5

def test_finance_entity_55_schema_validation():
    obj = FinanceSchemaEntity55Create(
        entity_code="TEST_FINANCE_55",
        name="Test Entity 55",
        value_amount=55 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_55"
    assert obj.value_amount == 55 * 100.5

def test_finance_entity_56_schema_validation():
    obj = FinanceSchemaEntity56Create(
        entity_code="TEST_FINANCE_56",
        name="Test Entity 56",
        value_amount=56 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_56"
    assert obj.value_amount == 56 * 100.5

def test_finance_entity_57_schema_validation():
    obj = FinanceSchemaEntity57Create(
        entity_code="TEST_FINANCE_57",
        name="Test Entity 57",
        value_amount=57 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_57"
    assert obj.value_amount == 57 * 100.5

def test_finance_entity_58_schema_validation():
    obj = FinanceSchemaEntity58Create(
        entity_code="TEST_FINANCE_58",
        name="Test Entity 58",
        value_amount=58 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_58"
    assert obj.value_amount == 58 * 100.5

def test_finance_entity_59_schema_validation():
    obj = FinanceSchemaEntity59Create(
        entity_code="TEST_FINANCE_59",
        name="Test Entity 59",
        value_amount=59 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_59"
    assert obj.value_amount == 59 * 100.5

def test_finance_entity_60_schema_validation():
    obj = FinanceSchemaEntity60Create(
        entity_code="TEST_FINANCE_60",
        name="Test Entity 60",
        value_amount=60 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_60"
    assert obj.value_amount == 60 * 100.5

def test_finance_entity_61_schema_validation():
    obj = FinanceSchemaEntity61Create(
        entity_code="TEST_FINANCE_61",
        name="Test Entity 61",
        value_amount=61 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_61"
    assert obj.value_amount == 61 * 100.5

def test_finance_entity_62_schema_validation():
    obj = FinanceSchemaEntity62Create(
        entity_code="TEST_FINANCE_62",
        name="Test Entity 62",
        value_amount=62 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_62"
    assert obj.value_amount == 62 * 100.5

def test_finance_entity_63_schema_validation():
    obj = FinanceSchemaEntity63Create(
        entity_code="TEST_FINANCE_63",
        name="Test Entity 63",
        value_amount=63 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_63"
    assert obj.value_amount == 63 * 100.5

def test_finance_entity_64_schema_validation():
    obj = FinanceSchemaEntity64Create(
        entity_code="TEST_FINANCE_64",
        name="Test Entity 64",
        value_amount=64 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_64"
    assert obj.value_amount == 64 * 100.5

def test_finance_entity_65_schema_validation():
    obj = FinanceSchemaEntity65Create(
        entity_code="TEST_FINANCE_65",
        name="Test Entity 65",
        value_amount=65 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_65"
    assert obj.value_amount == 65 * 100.5

def test_finance_entity_66_schema_validation():
    obj = FinanceSchemaEntity66Create(
        entity_code="TEST_FINANCE_66",
        name="Test Entity 66",
        value_amount=66 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_66"
    assert obj.value_amount == 66 * 100.5

def test_finance_entity_67_schema_validation():
    obj = FinanceSchemaEntity67Create(
        entity_code="TEST_FINANCE_67",
        name="Test Entity 67",
        value_amount=67 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_67"
    assert obj.value_amount == 67 * 100.5

def test_finance_entity_68_schema_validation():
    obj = FinanceSchemaEntity68Create(
        entity_code="TEST_FINANCE_68",
        name="Test Entity 68",
        value_amount=68 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_68"
    assert obj.value_amount == 68 * 100.5

def test_finance_entity_69_schema_validation():
    obj = FinanceSchemaEntity69Create(
        entity_code="TEST_FINANCE_69",
        name="Test Entity 69",
        value_amount=69 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_69"
    assert obj.value_amount == 69 * 100.5

def test_finance_entity_70_schema_validation():
    obj = FinanceSchemaEntity70Create(
        entity_code="TEST_FINANCE_70",
        name="Test Entity 70",
        value_amount=70 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_70"
    assert obj.value_amount == 70 * 100.5

def test_finance_entity_71_schema_validation():
    obj = FinanceSchemaEntity71Create(
        entity_code="TEST_FINANCE_71",
        name="Test Entity 71",
        value_amount=71 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_71"
    assert obj.value_amount == 71 * 100.5

def test_finance_entity_72_schema_validation():
    obj = FinanceSchemaEntity72Create(
        entity_code="TEST_FINANCE_72",
        name="Test Entity 72",
        value_amount=72 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_72"
    assert obj.value_amount == 72 * 100.5

def test_finance_entity_73_schema_validation():
    obj = FinanceSchemaEntity73Create(
        entity_code="TEST_FINANCE_73",
        name="Test Entity 73",
        value_amount=73 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_73"
    assert obj.value_amount == 73 * 100.5

def test_finance_entity_74_schema_validation():
    obj = FinanceSchemaEntity74Create(
        entity_code="TEST_FINANCE_74",
        name="Test Entity 74",
        value_amount=74 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_74"
    assert obj.value_amount == 74 * 100.5

def test_finance_entity_75_schema_validation():
    obj = FinanceSchemaEntity75Create(
        entity_code="TEST_FINANCE_75",
        name="Test Entity 75",
        value_amount=75 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_75"
    assert obj.value_amount == 75 * 100.5

def test_finance_entity_76_schema_validation():
    obj = FinanceSchemaEntity76Create(
        entity_code="TEST_FINANCE_76",
        name="Test Entity 76",
        value_amount=76 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_76"
    assert obj.value_amount == 76 * 100.5

def test_finance_entity_77_schema_validation():
    obj = FinanceSchemaEntity77Create(
        entity_code="TEST_FINANCE_77",
        name="Test Entity 77",
        value_amount=77 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_77"
    assert obj.value_amount == 77 * 100.5

def test_finance_entity_78_schema_validation():
    obj = FinanceSchemaEntity78Create(
        entity_code="TEST_FINANCE_78",
        name="Test Entity 78",
        value_amount=78 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_78"
    assert obj.value_amount == 78 * 100.5

def test_finance_entity_79_schema_validation():
    obj = FinanceSchemaEntity79Create(
        entity_code="TEST_FINANCE_79",
        name="Test Entity 79",
        value_amount=79 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_79"
    assert obj.value_amount == 79 * 100.5

def test_finance_entity_80_schema_validation():
    obj = FinanceSchemaEntity80Create(
        entity_code="TEST_FINANCE_80",
        name="Test Entity 80",
        value_amount=80 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_80"
    assert obj.value_amount == 80 * 100.5

def test_finance_entity_81_schema_validation():
    obj = FinanceSchemaEntity81Create(
        entity_code="TEST_FINANCE_81",
        name="Test Entity 81",
        value_amount=81 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_81"
    assert obj.value_amount == 81 * 100.5

def test_finance_entity_82_schema_validation():
    obj = FinanceSchemaEntity82Create(
        entity_code="TEST_FINANCE_82",
        name="Test Entity 82",
        value_amount=82 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_82"
    assert obj.value_amount == 82 * 100.5

def test_finance_entity_83_schema_validation():
    obj = FinanceSchemaEntity83Create(
        entity_code="TEST_FINANCE_83",
        name="Test Entity 83",
        value_amount=83 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_83"
    assert obj.value_amount == 83 * 100.5

def test_finance_entity_84_schema_validation():
    obj = FinanceSchemaEntity84Create(
        entity_code="TEST_FINANCE_84",
        name="Test Entity 84",
        value_amount=84 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_84"
    assert obj.value_amount == 84 * 100.5

def test_finance_entity_85_schema_validation():
    obj = FinanceSchemaEntity85Create(
        entity_code="TEST_FINANCE_85",
        name="Test Entity 85",
        value_amount=85 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_85"
    assert obj.value_amount == 85 * 100.5

def test_finance_entity_86_schema_validation():
    obj = FinanceSchemaEntity86Create(
        entity_code="TEST_FINANCE_86",
        name="Test Entity 86",
        value_amount=86 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_86"
    assert obj.value_amount == 86 * 100.5

def test_finance_entity_87_schema_validation():
    obj = FinanceSchemaEntity87Create(
        entity_code="TEST_FINANCE_87",
        name="Test Entity 87",
        value_amount=87 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_87"
    assert obj.value_amount == 87 * 100.5

def test_finance_entity_88_schema_validation():
    obj = FinanceSchemaEntity88Create(
        entity_code="TEST_FINANCE_88",
        name="Test Entity 88",
        value_amount=88 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_88"
    assert obj.value_amount == 88 * 100.5

def test_finance_entity_89_schema_validation():
    obj = FinanceSchemaEntity89Create(
        entity_code="TEST_FINANCE_89",
        name="Test Entity 89",
        value_amount=89 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_89"
    assert obj.value_amount == 89 * 100.5

def test_finance_entity_90_schema_validation():
    obj = FinanceSchemaEntity90Create(
        entity_code="TEST_FINANCE_90",
        name="Test Entity 90",
        value_amount=90 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_90"
    assert obj.value_amount == 90 * 100.5

def test_finance_entity_91_schema_validation():
    obj = FinanceSchemaEntity91Create(
        entity_code="TEST_FINANCE_91",
        name="Test Entity 91",
        value_amount=91 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_91"
    assert obj.value_amount == 91 * 100.5

def test_finance_entity_92_schema_validation():
    obj = FinanceSchemaEntity92Create(
        entity_code="TEST_FINANCE_92",
        name="Test Entity 92",
        value_amount=92 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_92"
    assert obj.value_amount == 92 * 100.5

def test_finance_entity_93_schema_validation():
    obj = FinanceSchemaEntity93Create(
        entity_code="TEST_FINANCE_93",
        name="Test Entity 93",
        value_amount=93 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_93"
    assert obj.value_amount == 93 * 100.5

def test_finance_entity_94_schema_validation():
    obj = FinanceSchemaEntity94Create(
        entity_code="TEST_FINANCE_94",
        name="Test Entity 94",
        value_amount=94 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_94"
    assert obj.value_amount == 94 * 100.5

def test_finance_entity_95_schema_validation():
    obj = FinanceSchemaEntity95Create(
        entity_code="TEST_FINANCE_95",
        name="Test Entity 95",
        value_amount=95 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_95"
    assert obj.value_amount == 95 * 100.5

def test_finance_entity_96_schema_validation():
    obj = FinanceSchemaEntity96Create(
        entity_code="TEST_FINANCE_96",
        name="Test Entity 96",
        value_amount=96 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_96"
    assert obj.value_amount == 96 * 100.5

def test_finance_entity_97_schema_validation():
    obj = FinanceSchemaEntity97Create(
        entity_code="TEST_FINANCE_97",
        name="Test Entity 97",
        value_amount=97 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_97"
    assert obj.value_amount == 97 * 100.5

def test_finance_entity_98_schema_validation():
    obj = FinanceSchemaEntity98Create(
        entity_code="TEST_FINANCE_98",
        name="Test Entity 98",
        value_amount=98 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_98"
    assert obj.value_amount == 98 * 100.5

def test_finance_entity_99_schema_validation():
    obj = FinanceSchemaEntity99Create(
        entity_code="TEST_FINANCE_99",
        name="Test Entity 99",
        value_amount=99 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_99"
    assert obj.value_amount == 99 * 100.5

def test_finance_entity_100_schema_validation():
    obj = FinanceSchemaEntity100Create(
        entity_code="TEST_FINANCE_100",
        name="Test Entity 100",
        value_amount=100 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_100"
    assert obj.value_amount == 100 * 100.5

def test_finance_entity_101_schema_validation():
    obj = FinanceSchemaEntity101Create(
        entity_code="TEST_FINANCE_101",
        name="Test Entity 101",
        value_amount=101 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_101"
    assert obj.value_amount == 101 * 100.5

def test_finance_entity_102_schema_validation():
    obj = FinanceSchemaEntity102Create(
        entity_code="TEST_FINANCE_102",
        name="Test Entity 102",
        value_amount=102 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_102"
    assert obj.value_amount == 102 * 100.5

def test_finance_entity_103_schema_validation():
    obj = FinanceSchemaEntity103Create(
        entity_code="TEST_FINANCE_103",
        name="Test Entity 103",
        value_amount=103 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_103"
    assert obj.value_amount == 103 * 100.5

def test_finance_entity_104_schema_validation():
    obj = FinanceSchemaEntity104Create(
        entity_code="TEST_FINANCE_104",
        name="Test Entity 104",
        value_amount=104 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_104"
    assert obj.value_amount == 104 * 100.5

def test_finance_entity_105_schema_validation():
    obj = FinanceSchemaEntity105Create(
        entity_code="TEST_FINANCE_105",
        name="Test Entity 105",
        value_amount=105 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_105"
    assert obj.value_amount == 105 * 100.5

def test_finance_entity_106_schema_validation():
    obj = FinanceSchemaEntity106Create(
        entity_code="TEST_FINANCE_106",
        name="Test Entity 106",
        value_amount=106 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_106"
    assert obj.value_amount == 106 * 100.5

def test_finance_entity_107_schema_validation():
    obj = FinanceSchemaEntity107Create(
        entity_code="TEST_FINANCE_107",
        name="Test Entity 107",
        value_amount=107 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_107"
    assert obj.value_amount == 107 * 100.5

def test_finance_entity_108_schema_validation():
    obj = FinanceSchemaEntity108Create(
        entity_code="TEST_FINANCE_108",
        name="Test Entity 108",
        value_amount=108 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_108"
    assert obj.value_amount == 108 * 100.5

def test_finance_entity_109_schema_validation():
    obj = FinanceSchemaEntity109Create(
        entity_code="TEST_FINANCE_109",
        name="Test Entity 109",
        value_amount=109 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_109"
    assert obj.value_amount == 109 * 100.5

def test_finance_entity_110_schema_validation():
    obj = FinanceSchemaEntity110Create(
        entity_code="TEST_FINANCE_110",
        name="Test Entity 110",
        value_amount=110 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_110"
    assert obj.value_amount == 110 * 100.5

def test_finance_entity_111_schema_validation():
    obj = FinanceSchemaEntity111Create(
        entity_code="TEST_FINANCE_111",
        name="Test Entity 111",
        value_amount=111 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_111"
    assert obj.value_amount == 111 * 100.5

def test_finance_entity_112_schema_validation():
    obj = FinanceSchemaEntity112Create(
        entity_code="TEST_FINANCE_112",
        name="Test Entity 112",
        value_amount=112 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_112"
    assert obj.value_amount == 112 * 100.5

def test_finance_entity_113_schema_validation():
    obj = FinanceSchemaEntity113Create(
        entity_code="TEST_FINANCE_113",
        name="Test Entity 113",
        value_amount=113 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_113"
    assert obj.value_amount == 113 * 100.5

def test_finance_entity_114_schema_validation():
    obj = FinanceSchemaEntity114Create(
        entity_code="TEST_FINANCE_114",
        name="Test Entity 114",
        value_amount=114 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_114"
    assert obj.value_amount == 114 * 100.5

def test_finance_entity_115_schema_validation():
    obj = FinanceSchemaEntity115Create(
        entity_code="TEST_FINANCE_115",
        name="Test Entity 115",
        value_amount=115 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_115"
    assert obj.value_amount == 115 * 100.5

def test_finance_entity_116_schema_validation():
    obj = FinanceSchemaEntity116Create(
        entity_code="TEST_FINANCE_116",
        name="Test Entity 116",
        value_amount=116 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_116"
    assert obj.value_amount == 116 * 100.5

def test_finance_entity_117_schema_validation():
    obj = FinanceSchemaEntity117Create(
        entity_code="TEST_FINANCE_117",
        name="Test Entity 117",
        value_amount=117 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_117"
    assert obj.value_amount == 117 * 100.5

def test_finance_entity_118_schema_validation():
    obj = FinanceSchemaEntity118Create(
        entity_code="TEST_FINANCE_118",
        name="Test Entity 118",
        value_amount=118 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_118"
    assert obj.value_amount == 118 * 100.5

def test_finance_entity_119_schema_validation():
    obj = FinanceSchemaEntity119Create(
        entity_code="TEST_FINANCE_119",
        name="Test Entity 119",
        value_amount=119 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_119"
    assert obj.value_amount == 119 * 100.5

def test_finance_entity_120_schema_validation():
    obj = FinanceSchemaEntity120Create(
        entity_code="TEST_FINANCE_120",
        name="Test Entity 120",
        value_amount=120 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_120"
    assert obj.value_amount == 120 * 100.5

def test_finance_entity_121_schema_validation():
    obj = FinanceSchemaEntity121Create(
        entity_code="TEST_FINANCE_121",
        name="Test Entity 121",
        value_amount=121 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_121"
    assert obj.value_amount == 121 * 100.5

def test_finance_entity_122_schema_validation():
    obj = FinanceSchemaEntity122Create(
        entity_code="TEST_FINANCE_122",
        name="Test Entity 122",
        value_amount=122 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_122"
    assert obj.value_amount == 122 * 100.5

def test_finance_entity_123_schema_validation():
    obj = FinanceSchemaEntity123Create(
        entity_code="TEST_FINANCE_123",
        name="Test Entity 123",
        value_amount=123 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_123"
    assert obj.value_amount == 123 * 100.5

def test_finance_entity_124_schema_validation():
    obj = FinanceSchemaEntity124Create(
        entity_code="TEST_FINANCE_124",
        name="Test Entity 124",
        value_amount=124 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_124"
    assert obj.value_amount == 124 * 100.5

def test_finance_entity_125_schema_validation():
    obj = FinanceSchemaEntity125Create(
        entity_code="TEST_FINANCE_125",
        name="Test Entity 125",
        value_amount=125 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_125"
    assert obj.value_amount == 125 * 100.5

def test_finance_entity_126_schema_validation():
    obj = FinanceSchemaEntity126Create(
        entity_code="TEST_FINANCE_126",
        name="Test Entity 126",
        value_amount=126 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_126"
    assert obj.value_amount == 126 * 100.5

def test_finance_entity_127_schema_validation():
    obj = FinanceSchemaEntity127Create(
        entity_code="TEST_FINANCE_127",
        name="Test Entity 127",
        value_amount=127 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_127"
    assert obj.value_amount == 127 * 100.5

def test_finance_entity_128_schema_validation():
    obj = FinanceSchemaEntity128Create(
        entity_code="TEST_FINANCE_128",
        name="Test Entity 128",
        value_amount=128 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_128"
    assert obj.value_amount == 128 * 100.5

def test_finance_entity_129_schema_validation():
    obj = FinanceSchemaEntity129Create(
        entity_code="TEST_FINANCE_129",
        name="Test Entity 129",
        value_amount=129 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_129"
    assert obj.value_amount == 129 * 100.5

def test_finance_entity_130_schema_validation():
    obj = FinanceSchemaEntity130Create(
        entity_code="TEST_FINANCE_130",
        name="Test Entity 130",
        value_amount=130 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_130"
    assert obj.value_amount == 130 * 100.5

def test_finance_entity_131_schema_validation():
    obj = FinanceSchemaEntity131Create(
        entity_code="TEST_FINANCE_131",
        name="Test Entity 131",
        value_amount=131 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_131"
    assert obj.value_amount == 131 * 100.5

def test_finance_entity_132_schema_validation():
    obj = FinanceSchemaEntity132Create(
        entity_code="TEST_FINANCE_132",
        name="Test Entity 132",
        value_amount=132 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_132"
    assert obj.value_amount == 132 * 100.5

def test_finance_entity_133_schema_validation():
    obj = FinanceSchemaEntity133Create(
        entity_code="TEST_FINANCE_133",
        name="Test Entity 133",
        value_amount=133 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_133"
    assert obj.value_amount == 133 * 100.5

def test_finance_entity_134_schema_validation():
    obj = FinanceSchemaEntity134Create(
        entity_code="TEST_FINANCE_134",
        name="Test Entity 134",
        value_amount=134 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_134"
    assert obj.value_amount == 134 * 100.5

def test_finance_entity_135_schema_validation():
    obj = FinanceSchemaEntity135Create(
        entity_code="TEST_FINANCE_135",
        name="Test Entity 135",
        value_amount=135 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_135"
    assert obj.value_amount == 135 * 100.5

def test_finance_entity_136_schema_validation():
    obj = FinanceSchemaEntity136Create(
        entity_code="TEST_FINANCE_136",
        name="Test Entity 136",
        value_amount=136 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_136"
    assert obj.value_amount == 136 * 100.5

def test_finance_entity_137_schema_validation():
    obj = FinanceSchemaEntity137Create(
        entity_code="TEST_FINANCE_137",
        name="Test Entity 137",
        value_amount=137 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_137"
    assert obj.value_amount == 137 * 100.5

def test_finance_entity_138_schema_validation():
    obj = FinanceSchemaEntity138Create(
        entity_code="TEST_FINANCE_138",
        name="Test Entity 138",
        value_amount=138 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_138"
    assert obj.value_amount == 138 * 100.5

def test_finance_entity_139_schema_validation():
    obj = FinanceSchemaEntity139Create(
        entity_code="TEST_FINANCE_139",
        name="Test Entity 139",
        value_amount=139 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_139"
    assert obj.value_amount == 139 * 100.5

def test_finance_entity_140_schema_validation():
    obj = FinanceSchemaEntity140Create(
        entity_code="TEST_FINANCE_140",
        name="Test Entity 140",
        value_amount=140 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_140"
    assert obj.value_amount == 140 * 100.5

def test_finance_entity_141_schema_validation():
    obj = FinanceSchemaEntity141Create(
        entity_code="TEST_FINANCE_141",
        name="Test Entity 141",
        value_amount=141 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_141"
    assert obj.value_amount == 141 * 100.5

def test_finance_entity_142_schema_validation():
    obj = FinanceSchemaEntity142Create(
        entity_code="TEST_FINANCE_142",
        name="Test Entity 142",
        value_amount=142 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_142"
    assert obj.value_amount == 142 * 100.5

def test_finance_entity_143_schema_validation():
    obj = FinanceSchemaEntity143Create(
        entity_code="TEST_FINANCE_143",
        name="Test Entity 143",
        value_amount=143 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_143"
    assert obj.value_amount == 143 * 100.5

def test_finance_entity_144_schema_validation():
    obj = FinanceSchemaEntity144Create(
        entity_code="TEST_FINANCE_144",
        name="Test Entity 144",
        value_amount=144 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_144"
    assert obj.value_amount == 144 * 100.5

def test_finance_entity_145_schema_validation():
    obj = FinanceSchemaEntity145Create(
        entity_code="TEST_FINANCE_145",
        name="Test Entity 145",
        value_amount=145 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_145"
    assert obj.value_amount == 145 * 100.5

def test_finance_entity_146_schema_validation():
    obj = FinanceSchemaEntity146Create(
        entity_code="TEST_FINANCE_146",
        name="Test Entity 146",
        value_amount=146 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_146"
    assert obj.value_amount == 146 * 100.5

def test_finance_entity_147_schema_validation():
    obj = FinanceSchemaEntity147Create(
        entity_code="TEST_FINANCE_147",
        name="Test Entity 147",
        value_amount=147 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_147"
    assert obj.value_amount == 147 * 100.5

def test_finance_entity_148_schema_validation():
    obj = FinanceSchemaEntity148Create(
        entity_code="TEST_FINANCE_148",
        name="Test Entity 148",
        value_amount=148 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_148"
    assert obj.value_amount == 148 * 100.5

def test_finance_entity_149_schema_validation():
    obj = FinanceSchemaEntity149Create(
        entity_code="TEST_FINANCE_149",
        name="Test Entity 149",
        value_amount=149 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_149"
    assert obj.value_amount == 149 * 100.5

def test_finance_entity_150_schema_validation():
    obj = FinanceSchemaEntity150Create(
        entity_code="TEST_FINANCE_150",
        name="Test Entity 150",
        value_amount=150 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_150"
    assert obj.value_amount == 150 * 100.5

def test_finance_entity_151_schema_validation():
    obj = FinanceSchemaEntity151Create(
        entity_code="TEST_FINANCE_151",
        name="Test Entity 151",
        value_amount=151 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_151"
    assert obj.value_amount == 151 * 100.5

def test_finance_entity_152_schema_validation():
    obj = FinanceSchemaEntity152Create(
        entity_code="TEST_FINANCE_152",
        name="Test Entity 152",
        value_amount=152 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_152"
    assert obj.value_amount == 152 * 100.5

def test_finance_entity_153_schema_validation():
    obj = FinanceSchemaEntity153Create(
        entity_code="TEST_FINANCE_153",
        name="Test Entity 153",
        value_amount=153 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_153"
    assert obj.value_amount == 153 * 100.5

def test_finance_entity_154_schema_validation():
    obj = FinanceSchemaEntity154Create(
        entity_code="TEST_FINANCE_154",
        name="Test Entity 154",
        value_amount=154 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_154"
    assert obj.value_amount == 154 * 100.5

def test_finance_entity_155_schema_validation():
    obj = FinanceSchemaEntity155Create(
        entity_code="TEST_FINANCE_155",
        name="Test Entity 155",
        value_amount=155 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_155"
    assert obj.value_amount == 155 * 100.5

def test_finance_entity_156_schema_validation():
    obj = FinanceSchemaEntity156Create(
        entity_code="TEST_FINANCE_156",
        name="Test Entity 156",
        value_amount=156 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_156"
    assert obj.value_amount == 156 * 100.5

def test_finance_entity_157_schema_validation():
    obj = FinanceSchemaEntity157Create(
        entity_code="TEST_FINANCE_157",
        name="Test Entity 157",
        value_amount=157 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_157"
    assert obj.value_amount == 157 * 100.5

def test_finance_entity_158_schema_validation():
    obj = FinanceSchemaEntity158Create(
        entity_code="TEST_FINANCE_158",
        name="Test Entity 158",
        value_amount=158 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_158"
    assert obj.value_amount == 158 * 100.5

def test_finance_entity_159_schema_validation():
    obj = FinanceSchemaEntity159Create(
        entity_code="TEST_FINANCE_159",
        name="Test Entity 159",
        value_amount=159 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_159"
    assert obj.value_amount == 159 * 100.5

def test_finance_entity_160_schema_validation():
    obj = FinanceSchemaEntity160Create(
        entity_code="TEST_FINANCE_160",
        name="Test Entity 160",
        value_amount=160 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_160"
    assert obj.value_amount == 160 * 100.5

def test_finance_entity_161_schema_validation():
    obj = FinanceSchemaEntity161Create(
        entity_code="TEST_FINANCE_161",
        name="Test Entity 161",
        value_amount=161 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_161"
    assert obj.value_amount == 161 * 100.5

def test_finance_entity_162_schema_validation():
    obj = FinanceSchemaEntity162Create(
        entity_code="TEST_FINANCE_162",
        name="Test Entity 162",
        value_amount=162 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_162"
    assert obj.value_amount == 162 * 100.5

def test_finance_entity_163_schema_validation():
    obj = FinanceSchemaEntity163Create(
        entity_code="TEST_FINANCE_163",
        name="Test Entity 163",
        value_amount=163 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_163"
    assert obj.value_amount == 163 * 100.5

def test_finance_entity_164_schema_validation():
    obj = FinanceSchemaEntity164Create(
        entity_code="TEST_FINANCE_164",
        name="Test Entity 164",
        value_amount=164 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_164"
    assert obj.value_amount == 164 * 100.5

def test_finance_entity_165_schema_validation():
    obj = FinanceSchemaEntity165Create(
        entity_code="TEST_FINANCE_165",
        name="Test Entity 165",
        value_amount=165 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_165"
    assert obj.value_amount == 165 * 100.5

def test_finance_entity_166_schema_validation():
    obj = FinanceSchemaEntity166Create(
        entity_code="TEST_FINANCE_166",
        name="Test Entity 166",
        value_amount=166 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_166"
    assert obj.value_amount == 166 * 100.5

def test_finance_entity_167_schema_validation():
    obj = FinanceSchemaEntity167Create(
        entity_code="TEST_FINANCE_167",
        name="Test Entity 167",
        value_amount=167 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_167"
    assert obj.value_amount == 167 * 100.5

def test_finance_entity_168_schema_validation():
    obj = FinanceSchemaEntity168Create(
        entity_code="TEST_FINANCE_168",
        name="Test Entity 168",
        value_amount=168 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_168"
    assert obj.value_amount == 168 * 100.5

def test_finance_entity_169_schema_validation():
    obj = FinanceSchemaEntity169Create(
        entity_code="TEST_FINANCE_169",
        name="Test Entity 169",
        value_amount=169 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_169"
    assert obj.value_amount == 169 * 100.5

def test_finance_entity_170_schema_validation():
    obj = FinanceSchemaEntity170Create(
        entity_code="TEST_FINANCE_170",
        name="Test Entity 170",
        value_amount=170 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_170"
    assert obj.value_amount == 170 * 100.5

def test_finance_entity_171_schema_validation():
    obj = FinanceSchemaEntity171Create(
        entity_code="TEST_FINANCE_171",
        name="Test Entity 171",
        value_amount=171 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_171"
    assert obj.value_amount == 171 * 100.5

def test_finance_entity_172_schema_validation():
    obj = FinanceSchemaEntity172Create(
        entity_code="TEST_FINANCE_172",
        name="Test Entity 172",
        value_amount=172 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_172"
    assert obj.value_amount == 172 * 100.5

def test_finance_entity_173_schema_validation():
    obj = FinanceSchemaEntity173Create(
        entity_code="TEST_FINANCE_173",
        name="Test Entity 173",
        value_amount=173 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_173"
    assert obj.value_amount == 173 * 100.5

def test_finance_entity_174_schema_validation():
    obj = FinanceSchemaEntity174Create(
        entity_code="TEST_FINANCE_174",
        name="Test Entity 174",
        value_amount=174 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_174"
    assert obj.value_amount == 174 * 100.5

def test_finance_entity_175_schema_validation():
    obj = FinanceSchemaEntity175Create(
        entity_code="TEST_FINANCE_175",
        name="Test Entity 175",
        value_amount=175 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_175"
    assert obj.value_amount == 175 * 100.5

def test_finance_entity_176_schema_validation():
    obj = FinanceSchemaEntity176Create(
        entity_code="TEST_FINANCE_176",
        name="Test Entity 176",
        value_amount=176 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_176"
    assert obj.value_amount == 176 * 100.5

def test_finance_entity_177_schema_validation():
    obj = FinanceSchemaEntity177Create(
        entity_code="TEST_FINANCE_177",
        name="Test Entity 177",
        value_amount=177 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_177"
    assert obj.value_amount == 177 * 100.5

def test_finance_entity_178_schema_validation():
    obj = FinanceSchemaEntity178Create(
        entity_code="TEST_FINANCE_178",
        name="Test Entity 178",
        value_amount=178 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_178"
    assert obj.value_amount == 178 * 100.5

def test_finance_entity_179_schema_validation():
    obj = FinanceSchemaEntity179Create(
        entity_code="TEST_FINANCE_179",
        name="Test Entity 179",
        value_amount=179 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_179"
    assert obj.value_amount == 179 * 100.5

def test_finance_entity_180_schema_validation():
    obj = FinanceSchemaEntity180Create(
        entity_code="TEST_FINANCE_180",
        name="Test Entity 180",
        value_amount=180 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_180"
    assert obj.value_amount == 180 * 100.5

def test_finance_entity_181_schema_validation():
    obj = FinanceSchemaEntity181Create(
        entity_code="TEST_FINANCE_181",
        name="Test Entity 181",
        value_amount=181 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_181"
    assert obj.value_amount == 181 * 100.5

def test_finance_entity_182_schema_validation():
    obj = FinanceSchemaEntity182Create(
        entity_code="TEST_FINANCE_182",
        name="Test Entity 182",
        value_amount=182 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_182"
    assert obj.value_amount == 182 * 100.5

def test_finance_entity_183_schema_validation():
    obj = FinanceSchemaEntity183Create(
        entity_code="TEST_FINANCE_183",
        name="Test Entity 183",
        value_amount=183 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_183"
    assert obj.value_amount == 183 * 100.5

def test_finance_entity_184_schema_validation():
    obj = FinanceSchemaEntity184Create(
        entity_code="TEST_FINANCE_184",
        name="Test Entity 184",
        value_amount=184 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_184"
    assert obj.value_amount == 184 * 100.5

def test_finance_entity_185_schema_validation():
    obj = FinanceSchemaEntity185Create(
        entity_code="TEST_FINANCE_185",
        name="Test Entity 185",
        value_amount=185 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_185"
    assert obj.value_amount == 185 * 100.5

def test_finance_entity_186_schema_validation():
    obj = FinanceSchemaEntity186Create(
        entity_code="TEST_FINANCE_186",
        name="Test Entity 186",
        value_amount=186 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_186"
    assert obj.value_amount == 186 * 100.5

def test_finance_entity_187_schema_validation():
    obj = FinanceSchemaEntity187Create(
        entity_code="TEST_FINANCE_187",
        name="Test Entity 187",
        value_amount=187 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_187"
    assert obj.value_amount == 187 * 100.5

def test_finance_entity_188_schema_validation():
    obj = FinanceSchemaEntity188Create(
        entity_code="TEST_FINANCE_188",
        name="Test Entity 188",
        value_amount=188 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_188"
    assert obj.value_amount == 188 * 100.5

def test_finance_entity_189_schema_validation():
    obj = FinanceSchemaEntity189Create(
        entity_code="TEST_FINANCE_189",
        name="Test Entity 189",
        value_amount=189 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_189"
    assert obj.value_amount == 189 * 100.5

def test_finance_entity_190_schema_validation():
    obj = FinanceSchemaEntity190Create(
        entity_code="TEST_FINANCE_190",
        name="Test Entity 190",
        value_amount=190 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_190"
    assert obj.value_amount == 190 * 100.5

def test_finance_entity_191_schema_validation():
    obj = FinanceSchemaEntity191Create(
        entity_code="TEST_FINANCE_191",
        name="Test Entity 191",
        value_amount=191 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_191"
    assert obj.value_amount == 191 * 100.5

def test_finance_entity_192_schema_validation():
    obj = FinanceSchemaEntity192Create(
        entity_code="TEST_FINANCE_192",
        name="Test Entity 192",
        value_amount=192 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_192"
    assert obj.value_amount == 192 * 100.5

def test_finance_entity_193_schema_validation():
    obj = FinanceSchemaEntity193Create(
        entity_code="TEST_FINANCE_193",
        name="Test Entity 193",
        value_amount=193 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_193"
    assert obj.value_amount == 193 * 100.5

def test_finance_entity_194_schema_validation():
    obj = FinanceSchemaEntity194Create(
        entity_code="TEST_FINANCE_194",
        name="Test Entity 194",
        value_amount=194 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_194"
    assert obj.value_amount == 194 * 100.5

def test_finance_entity_195_schema_validation():
    obj = FinanceSchemaEntity195Create(
        entity_code="TEST_FINANCE_195",
        name="Test Entity 195",
        value_amount=195 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_195"
    assert obj.value_amount == 195 * 100.5

def test_finance_entity_196_schema_validation():
    obj = FinanceSchemaEntity196Create(
        entity_code="TEST_FINANCE_196",
        name="Test Entity 196",
        value_amount=196 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_196"
    assert obj.value_amount == 196 * 100.5

def test_finance_entity_197_schema_validation():
    obj = FinanceSchemaEntity197Create(
        entity_code="TEST_FINANCE_197",
        name="Test Entity 197",
        value_amount=197 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_197"
    assert obj.value_amount == 197 * 100.5

def test_finance_entity_198_schema_validation():
    obj = FinanceSchemaEntity198Create(
        entity_code="TEST_FINANCE_198",
        name="Test Entity 198",
        value_amount=198 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_198"
    assert obj.value_amount == 198 * 100.5

def test_finance_entity_199_schema_validation():
    obj = FinanceSchemaEntity199Create(
        entity_code="TEST_FINANCE_199",
        name="Test Entity 199",
        value_amount=199 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_199"
    assert obj.value_amount == 199 * 100.5

def test_finance_entity_200_schema_validation():
    obj = FinanceSchemaEntity200Create(
        entity_code="TEST_FINANCE_200",
        name="Test Entity 200",
        value_amount=200 * 100.5
    )
    assert obj.entity_code == "TEST_FINANCE_200"
    assert obj.value_amount == 200 * 100.5


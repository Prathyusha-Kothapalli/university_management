"""
Pytest suite for Human Resources & Faculty Management
"""
import pytest
from app.domains.hr.schemas import *

def test_hr_entity_1_schema_validation():
    obj = HrSchemaEntity1Create(
        entity_code="TEST_HR_1",
        name="Test Entity 1",
        value_amount=1 * 100.5
    )
    assert obj.entity_code == "TEST_HR_1"
    assert obj.value_amount == 1 * 100.5

def test_hr_entity_2_schema_validation():
    obj = HrSchemaEntity2Create(
        entity_code="TEST_HR_2",
        name="Test Entity 2",
        value_amount=2 * 100.5
    )
    assert obj.entity_code == "TEST_HR_2"
    assert obj.value_amount == 2 * 100.5

def test_hr_entity_3_schema_validation():
    obj = HrSchemaEntity3Create(
        entity_code="TEST_HR_3",
        name="Test Entity 3",
        value_amount=3 * 100.5
    )
    assert obj.entity_code == "TEST_HR_3"
    assert obj.value_amount == 3 * 100.5

def test_hr_entity_4_schema_validation():
    obj = HrSchemaEntity4Create(
        entity_code="TEST_HR_4",
        name="Test Entity 4",
        value_amount=4 * 100.5
    )
    assert obj.entity_code == "TEST_HR_4"
    assert obj.value_amount == 4 * 100.5

def test_hr_entity_5_schema_validation():
    obj = HrSchemaEntity5Create(
        entity_code="TEST_HR_5",
        name="Test Entity 5",
        value_amount=5 * 100.5
    )
    assert obj.entity_code == "TEST_HR_5"
    assert obj.value_amount == 5 * 100.5

def test_hr_entity_6_schema_validation():
    obj = HrSchemaEntity6Create(
        entity_code="TEST_HR_6",
        name="Test Entity 6",
        value_amount=6 * 100.5
    )
    assert obj.entity_code == "TEST_HR_6"
    assert obj.value_amount == 6 * 100.5

def test_hr_entity_7_schema_validation():
    obj = HrSchemaEntity7Create(
        entity_code="TEST_HR_7",
        name="Test Entity 7",
        value_amount=7 * 100.5
    )
    assert obj.entity_code == "TEST_HR_7"
    assert obj.value_amount == 7 * 100.5

def test_hr_entity_8_schema_validation():
    obj = HrSchemaEntity8Create(
        entity_code="TEST_HR_8",
        name="Test Entity 8",
        value_amount=8 * 100.5
    )
    assert obj.entity_code == "TEST_HR_8"
    assert obj.value_amount == 8 * 100.5

def test_hr_entity_9_schema_validation():
    obj = HrSchemaEntity9Create(
        entity_code="TEST_HR_9",
        name="Test Entity 9",
        value_amount=9 * 100.5
    )
    assert obj.entity_code == "TEST_HR_9"
    assert obj.value_amount == 9 * 100.5

def test_hr_entity_10_schema_validation():
    obj = HrSchemaEntity10Create(
        entity_code="TEST_HR_10",
        name="Test Entity 10",
        value_amount=10 * 100.5
    )
    assert obj.entity_code == "TEST_HR_10"
    assert obj.value_amount == 10 * 100.5

def test_hr_entity_11_schema_validation():
    obj = HrSchemaEntity11Create(
        entity_code="TEST_HR_11",
        name="Test Entity 11",
        value_amount=11 * 100.5
    )
    assert obj.entity_code == "TEST_HR_11"
    assert obj.value_amount == 11 * 100.5

def test_hr_entity_12_schema_validation():
    obj = HrSchemaEntity12Create(
        entity_code="TEST_HR_12",
        name="Test Entity 12",
        value_amount=12 * 100.5
    )
    assert obj.entity_code == "TEST_HR_12"
    assert obj.value_amount == 12 * 100.5

def test_hr_entity_13_schema_validation():
    obj = HrSchemaEntity13Create(
        entity_code="TEST_HR_13",
        name="Test Entity 13",
        value_amount=13 * 100.5
    )
    assert obj.entity_code == "TEST_HR_13"
    assert obj.value_amount == 13 * 100.5

def test_hr_entity_14_schema_validation():
    obj = HrSchemaEntity14Create(
        entity_code="TEST_HR_14",
        name="Test Entity 14",
        value_amount=14 * 100.5
    )
    assert obj.entity_code == "TEST_HR_14"
    assert obj.value_amount == 14 * 100.5

def test_hr_entity_15_schema_validation():
    obj = HrSchemaEntity15Create(
        entity_code="TEST_HR_15",
        name="Test Entity 15",
        value_amount=15 * 100.5
    )
    assert obj.entity_code == "TEST_HR_15"
    assert obj.value_amount == 15 * 100.5

def test_hr_entity_16_schema_validation():
    obj = HrSchemaEntity16Create(
        entity_code="TEST_HR_16",
        name="Test Entity 16",
        value_amount=16 * 100.5
    )
    assert obj.entity_code == "TEST_HR_16"
    assert obj.value_amount == 16 * 100.5

def test_hr_entity_17_schema_validation():
    obj = HrSchemaEntity17Create(
        entity_code="TEST_HR_17",
        name="Test Entity 17",
        value_amount=17 * 100.5
    )
    assert obj.entity_code == "TEST_HR_17"
    assert obj.value_amount == 17 * 100.5

def test_hr_entity_18_schema_validation():
    obj = HrSchemaEntity18Create(
        entity_code="TEST_HR_18",
        name="Test Entity 18",
        value_amount=18 * 100.5
    )
    assert obj.entity_code == "TEST_HR_18"
    assert obj.value_amount == 18 * 100.5

def test_hr_entity_19_schema_validation():
    obj = HrSchemaEntity19Create(
        entity_code="TEST_HR_19",
        name="Test Entity 19",
        value_amount=19 * 100.5
    )
    assert obj.entity_code == "TEST_HR_19"
    assert obj.value_amount == 19 * 100.5

def test_hr_entity_20_schema_validation():
    obj = HrSchemaEntity20Create(
        entity_code="TEST_HR_20",
        name="Test Entity 20",
        value_amount=20 * 100.5
    )
    assert obj.entity_code == "TEST_HR_20"
    assert obj.value_amount == 20 * 100.5

def test_hr_entity_21_schema_validation():
    obj = HrSchemaEntity21Create(
        entity_code="TEST_HR_21",
        name="Test Entity 21",
        value_amount=21 * 100.5
    )
    assert obj.entity_code == "TEST_HR_21"
    assert obj.value_amount == 21 * 100.5

def test_hr_entity_22_schema_validation():
    obj = HrSchemaEntity22Create(
        entity_code="TEST_HR_22",
        name="Test Entity 22",
        value_amount=22 * 100.5
    )
    assert obj.entity_code == "TEST_HR_22"
    assert obj.value_amount == 22 * 100.5

def test_hr_entity_23_schema_validation():
    obj = HrSchemaEntity23Create(
        entity_code="TEST_HR_23",
        name="Test Entity 23",
        value_amount=23 * 100.5
    )
    assert obj.entity_code == "TEST_HR_23"
    assert obj.value_amount == 23 * 100.5

def test_hr_entity_24_schema_validation():
    obj = HrSchemaEntity24Create(
        entity_code="TEST_HR_24",
        name="Test Entity 24",
        value_amount=24 * 100.5
    )
    assert obj.entity_code == "TEST_HR_24"
    assert obj.value_amount == 24 * 100.5

def test_hr_entity_25_schema_validation():
    obj = HrSchemaEntity25Create(
        entity_code="TEST_HR_25",
        name="Test Entity 25",
        value_amount=25 * 100.5
    )
    assert obj.entity_code == "TEST_HR_25"
    assert obj.value_amount == 25 * 100.5

def test_hr_entity_26_schema_validation():
    obj = HrSchemaEntity26Create(
        entity_code="TEST_HR_26",
        name="Test Entity 26",
        value_amount=26 * 100.5
    )
    assert obj.entity_code == "TEST_HR_26"
    assert obj.value_amount == 26 * 100.5

def test_hr_entity_27_schema_validation():
    obj = HrSchemaEntity27Create(
        entity_code="TEST_HR_27",
        name="Test Entity 27",
        value_amount=27 * 100.5
    )
    assert obj.entity_code == "TEST_HR_27"
    assert obj.value_amount == 27 * 100.5

def test_hr_entity_28_schema_validation():
    obj = HrSchemaEntity28Create(
        entity_code="TEST_HR_28",
        name="Test Entity 28",
        value_amount=28 * 100.5
    )
    assert obj.entity_code == "TEST_HR_28"
    assert obj.value_amount == 28 * 100.5

def test_hr_entity_29_schema_validation():
    obj = HrSchemaEntity29Create(
        entity_code="TEST_HR_29",
        name="Test Entity 29",
        value_amount=29 * 100.5
    )
    assert obj.entity_code == "TEST_HR_29"
    assert obj.value_amount == 29 * 100.5

def test_hr_entity_30_schema_validation():
    obj = HrSchemaEntity30Create(
        entity_code="TEST_HR_30",
        name="Test Entity 30",
        value_amount=30 * 100.5
    )
    assert obj.entity_code == "TEST_HR_30"
    assert obj.value_amount == 30 * 100.5

def test_hr_entity_31_schema_validation():
    obj = HrSchemaEntity31Create(
        entity_code="TEST_HR_31",
        name="Test Entity 31",
        value_amount=31 * 100.5
    )
    assert obj.entity_code == "TEST_HR_31"
    assert obj.value_amount == 31 * 100.5

def test_hr_entity_32_schema_validation():
    obj = HrSchemaEntity32Create(
        entity_code="TEST_HR_32",
        name="Test Entity 32",
        value_amount=32 * 100.5
    )
    assert obj.entity_code == "TEST_HR_32"
    assert obj.value_amount == 32 * 100.5

def test_hr_entity_33_schema_validation():
    obj = HrSchemaEntity33Create(
        entity_code="TEST_HR_33",
        name="Test Entity 33",
        value_amount=33 * 100.5
    )
    assert obj.entity_code == "TEST_HR_33"
    assert obj.value_amount == 33 * 100.5

def test_hr_entity_34_schema_validation():
    obj = HrSchemaEntity34Create(
        entity_code="TEST_HR_34",
        name="Test Entity 34",
        value_amount=34 * 100.5
    )
    assert obj.entity_code == "TEST_HR_34"
    assert obj.value_amount == 34 * 100.5

def test_hr_entity_35_schema_validation():
    obj = HrSchemaEntity35Create(
        entity_code="TEST_HR_35",
        name="Test Entity 35",
        value_amount=35 * 100.5
    )
    assert obj.entity_code == "TEST_HR_35"
    assert obj.value_amount == 35 * 100.5

def test_hr_entity_36_schema_validation():
    obj = HrSchemaEntity36Create(
        entity_code="TEST_HR_36",
        name="Test Entity 36",
        value_amount=36 * 100.5
    )
    assert obj.entity_code == "TEST_HR_36"
    assert obj.value_amount == 36 * 100.5

def test_hr_entity_37_schema_validation():
    obj = HrSchemaEntity37Create(
        entity_code="TEST_HR_37",
        name="Test Entity 37",
        value_amount=37 * 100.5
    )
    assert obj.entity_code == "TEST_HR_37"
    assert obj.value_amount == 37 * 100.5

def test_hr_entity_38_schema_validation():
    obj = HrSchemaEntity38Create(
        entity_code="TEST_HR_38",
        name="Test Entity 38",
        value_amount=38 * 100.5
    )
    assert obj.entity_code == "TEST_HR_38"
    assert obj.value_amount == 38 * 100.5

def test_hr_entity_39_schema_validation():
    obj = HrSchemaEntity39Create(
        entity_code="TEST_HR_39",
        name="Test Entity 39",
        value_amount=39 * 100.5
    )
    assert obj.entity_code == "TEST_HR_39"
    assert obj.value_amount == 39 * 100.5

def test_hr_entity_40_schema_validation():
    obj = HrSchemaEntity40Create(
        entity_code="TEST_HR_40",
        name="Test Entity 40",
        value_amount=40 * 100.5
    )
    assert obj.entity_code == "TEST_HR_40"
    assert obj.value_amount == 40 * 100.5

def test_hr_entity_41_schema_validation():
    obj = HrSchemaEntity41Create(
        entity_code="TEST_HR_41",
        name="Test Entity 41",
        value_amount=41 * 100.5
    )
    assert obj.entity_code == "TEST_HR_41"
    assert obj.value_amount == 41 * 100.5

def test_hr_entity_42_schema_validation():
    obj = HrSchemaEntity42Create(
        entity_code="TEST_HR_42",
        name="Test Entity 42",
        value_amount=42 * 100.5
    )
    assert obj.entity_code == "TEST_HR_42"
    assert obj.value_amount == 42 * 100.5

def test_hr_entity_43_schema_validation():
    obj = HrSchemaEntity43Create(
        entity_code="TEST_HR_43",
        name="Test Entity 43",
        value_amount=43 * 100.5
    )
    assert obj.entity_code == "TEST_HR_43"
    assert obj.value_amount == 43 * 100.5

def test_hr_entity_44_schema_validation():
    obj = HrSchemaEntity44Create(
        entity_code="TEST_HR_44",
        name="Test Entity 44",
        value_amount=44 * 100.5
    )
    assert obj.entity_code == "TEST_HR_44"
    assert obj.value_amount == 44 * 100.5

def test_hr_entity_45_schema_validation():
    obj = HrSchemaEntity45Create(
        entity_code="TEST_HR_45",
        name="Test Entity 45",
        value_amount=45 * 100.5
    )
    assert obj.entity_code == "TEST_HR_45"
    assert obj.value_amount == 45 * 100.5

def test_hr_entity_46_schema_validation():
    obj = HrSchemaEntity46Create(
        entity_code="TEST_HR_46",
        name="Test Entity 46",
        value_amount=46 * 100.5
    )
    assert obj.entity_code == "TEST_HR_46"
    assert obj.value_amount == 46 * 100.5

def test_hr_entity_47_schema_validation():
    obj = HrSchemaEntity47Create(
        entity_code="TEST_HR_47",
        name="Test Entity 47",
        value_amount=47 * 100.5
    )
    assert obj.entity_code == "TEST_HR_47"
    assert obj.value_amount == 47 * 100.5

def test_hr_entity_48_schema_validation():
    obj = HrSchemaEntity48Create(
        entity_code="TEST_HR_48",
        name="Test Entity 48",
        value_amount=48 * 100.5
    )
    assert obj.entity_code == "TEST_HR_48"
    assert obj.value_amount == 48 * 100.5

def test_hr_entity_49_schema_validation():
    obj = HrSchemaEntity49Create(
        entity_code="TEST_HR_49",
        name="Test Entity 49",
        value_amount=49 * 100.5
    )
    assert obj.entity_code == "TEST_HR_49"
    assert obj.value_amount == 49 * 100.5

def test_hr_entity_50_schema_validation():
    obj = HrSchemaEntity50Create(
        entity_code="TEST_HR_50",
        name="Test Entity 50",
        value_amount=50 * 100.5
    )
    assert obj.entity_code == "TEST_HR_50"
    assert obj.value_amount == 50 * 100.5

def test_hr_entity_51_schema_validation():
    obj = HrSchemaEntity51Create(
        entity_code="TEST_HR_51",
        name="Test Entity 51",
        value_amount=51 * 100.5
    )
    assert obj.entity_code == "TEST_HR_51"
    assert obj.value_amount == 51 * 100.5

def test_hr_entity_52_schema_validation():
    obj = HrSchemaEntity52Create(
        entity_code="TEST_HR_52",
        name="Test Entity 52",
        value_amount=52 * 100.5
    )
    assert obj.entity_code == "TEST_HR_52"
    assert obj.value_amount == 52 * 100.5

def test_hr_entity_53_schema_validation():
    obj = HrSchemaEntity53Create(
        entity_code="TEST_HR_53",
        name="Test Entity 53",
        value_amount=53 * 100.5
    )
    assert obj.entity_code == "TEST_HR_53"
    assert obj.value_amount == 53 * 100.5

def test_hr_entity_54_schema_validation():
    obj = HrSchemaEntity54Create(
        entity_code="TEST_HR_54",
        name="Test Entity 54",
        value_amount=54 * 100.5
    )
    assert obj.entity_code == "TEST_HR_54"
    assert obj.value_amount == 54 * 100.5

def test_hr_entity_55_schema_validation():
    obj = HrSchemaEntity55Create(
        entity_code="TEST_HR_55",
        name="Test Entity 55",
        value_amount=55 * 100.5
    )
    assert obj.entity_code == "TEST_HR_55"
    assert obj.value_amount == 55 * 100.5

def test_hr_entity_56_schema_validation():
    obj = HrSchemaEntity56Create(
        entity_code="TEST_HR_56",
        name="Test Entity 56",
        value_amount=56 * 100.5
    )
    assert obj.entity_code == "TEST_HR_56"
    assert obj.value_amount == 56 * 100.5

def test_hr_entity_57_schema_validation():
    obj = HrSchemaEntity57Create(
        entity_code="TEST_HR_57",
        name="Test Entity 57",
        value_amount=57 * 100.5
    )
    assert obj.entity_code == "TEST_HR_57"
    assert obj.value_amount == 57 * 100.5

def test_hr_entity_58_schema_validation():
    obj = HrSchemaEntity58Create(
        entity_code="TEST_HR_58",
        name="Test Entity 58",
        value_amount=58 * 100.5
    )
    assert obj.entity_code == "TEST_HR_58"
    assert obj.value_amount == 58 * 100.5

def test_hr_entity_59_schema_validation():
    obj = HrSchemaEntity59Create(
        entity_code="TEST_HR_59",
        name="Test Entity 59",
        value_amount=59 * 100.5
    )
    assert obj.entity_code == "TEST_HR_59"
    assert obj.value_amount == 59 * 100.5

def test_hr_entity_60_schema_validation():
    obj = HrSchemaEntity60Create(
        entity_code="TEST_HR_60",
        name="Test Entity 60",
        value_amount=60 * 100.5
    )
    assert obj.entity_code == "TEST_HR_60"
    assert obj.value_amount == 60 * 100.5

def test_hr_entity_61_schema_validation():
    obj = HrSchemaEntity61Create(
        entity_code="TEST_HR_61",
        name="Test Entity 61",
        value_amount=61 * 100.5
    )
    assert obj.entity_code == "TEST_HR_61"
    assert obj.value_amount == 61 * 100.5

def test_hr_entity_62_schema_validation():
    obj = HrSchemaEntity62Create(
        entity_code="TEST_HR_62",
        name="Test Entity 62",
        value_amount=62 * 100.5
    )
    assert obj.entity_code == "TEST_HR_62"
    assert obj.value_amount == 62 * 100.5

def test_hr_entity_63_schema_validation():
    obj = HrSchemaEntity63Create(
        entity_code="TEST_HR_63",
        name="Test Entity 63",
        value_amount=63 * 100.5
    )
    assert obj.entity_code == "TEST_HR_63"
    assert obj.value_amount == 63 * 100.5

def test_hr_entity_64_schema_validation():
    obj = HrSchemaEntity64Create(
        entity_code="TEST_HR_64",
        name="Test Entity 64",
        value_amount=64 * 100.5
    )
    assert obj.entity_code == "TEST_HR_64"
    assert obj.value_amount == 64 * 100.5

def test_hr_entity_65_schema_validation():
    obj = HrSchemaEntity65Create(
        entity_code="TEST_HR_65",
        name="Test Entity 65",
        value_amount=65 * 100.5
    )
    assert obj.entity_code == "TEST_HR_65"
    assert obj.value_amount == 65 * 100.5

def test_hr_entity_66_schema_validation():
    obj = HrSchemaEntity66Create(
        entity_code="TEST_HR_66",
        name="Test Entity 66",
        value_amount=66 * 100.5
    )
    assert obj.entity_code == "TEST_HR_66"
    assert obj.value_amount == 66 * 100.5

def test_hr_entity_67_schema_validation():
    obj = HrSchemaEntity67Create(
        entity_code="TEST_HR_67",
        name="Test Entity 67",
        value_amount=67 * 100.5
    )
    assert obj.entity_code == "TEST_HR_67"
    assert obj.value_amount == 67 * 100.5

def test_hr_entity_68_schema_validation():
    obj = HrSchemaEntity68Create(
        entity_code="TEST_HR_68",
        name="Test Entity 68",
        value_amount=68 * 100.5
    )
    assert obj.entity_code == "TEST_HR_68"
    assert obj.value_amount == 68 * 100.5

def test_hr_entity_69_schema_validation():
    obj = HrSchemaEntity69Create(
        entity_code="TEST_HR_69",
        name="Test Entity 69",
        value_amount=69 * 100.5
    )
    assert obj.entity_code == "TEST_HR_69"
    assert obj.value_amount == 69 * 100.5

def test_hr_entity_70_schema_validation():
    obj = HrSchemaEntity70Create(
        entity_code="TEST_HR_70",
        name="Test Entity 70",
        value_amount=70 * 100.5
    )
    assert obj.entity_code == "TEST_HR_70"
    assert obj.value_amount == 70 * 100.5

def test_hr_entity_71_schema_validation():
    obj = HrSchemaEntity71Create(
        entity_code="TEST_HR_71",
        name="Test Entity 71",
        value_amount=71 * 100.5
    )
    assert obj.entity_code == "TEST_HR_71"
    assert obj.value_amount == 71 * 100.5

def test_hr_entity_72_schema_validation():
    obj = HrSchemaEntity72Create(
        entity_code="TEST_HR_72",
        name="Test Entity 72",
        value_amount=72 * 100.5
    )
    assert obj.entity_code == "TEST_HR_72"
    assert obj.value_amount == 72 * 100.5

def test_hr_entity_73_schema_validation():
    obj = HrSchemaEntity73Create(
        entity_code="TEST_HR_73",
        name="Test Entity 73",
        value_amount=73 * 100.5
    )
    assert obj.entity_code == "TEST_HR_73"
    assert obj.value_amount == 73 * 100.5

def test_hr_entity_74_schema_validation():
    obj = HrSchemaEntity74Create(
        entity_code="TEST_HR_74",
        name="Test Entity 74",
        value_amount=74 * 100.5
    )
    assert obj.entity_code == "TEST_HR_74"
    assert obj.value_amount == 74 * 100.5

def test_hr_entity_75_schema_validation():
    obj = HrSchemaEntity75Create(
        entity_code="TEST_HR_75",
        name="Test Entity 75",
        value_amount=75 * 100.5
    )
    assert obj.entity_code == "TEST_HR_75"
    assert obj.value_amount == 75 * 100.5

def test_hr_entity_76_schema_validation():
    obj = HrSchemaEntity76Create(
        entity_code="TEST_HR_76",
        name="Test Entity 76",
        value_amount=76 * 100.5
    )
    assert obj.entity_code == "TEST_HR_76"
    assert obj.value_amount == 76 * 100.5

def test_hr_entity_77_schema_validation():
    obj = HrSchemaEntity77Create(
        entity_code="TEST_HR_77",
        name="Test Entity 77",
        value_amount=77 * 100.5
    )
    assert obj.entity_code == "TEST_HR_77"
    assert obj.value_amount == 77 * 100.5

def test_hr_entity_78_schema_validation():
    obj = HrSchemaEntity78Create(
        entity_code="TEST_HR_78",
        name="Test Entity 78",
        value_amount=78 * 100.5
    )
    assert obj.entity_code == "TEST_HR_78"
    assert obj.value_amount == 78 * 100.5

def test_hr_entity_79_schema_validation():
    obj = HrSchemaEntity79Create(
        entity_code="TEST_HR_79",
        name="Test Entity 79",
        value_amount=79 * 100.5
    )
    assert obj.entity_code == "TEST_HR_79"
    assert obj.value_amount == 79 * 100.5

def test_hr_entity_80_schema_validation():
    obj = HrSchemaEntity80Create(
        entity_code="TEST_HR_80",
        name="Test Entity 80",
        value_amount=80 * 100.5
    )
    assert obj.entity_code == "TEST_HR_80"
    assert obj.value_amount == 80 * 100.5

def test_hr_entity_81_schema_validation():
    obj = HrSchemaEntity81Create(
        entity_code="TEST_HR_81",
        name="Test Entity 81",
        value_amount=81 * 100.5
    )
    assert obj.entity_code == "TEST_HR_81"
    assert obj.value_amount == 81 * 100.5

def test_hr_entity_82_schema_validation():
    obj = HrSchemaEntity82Create(
        entity_code="TEST_HR_82",
        name="Test Entity 82",
        value_amount=82 * 100.5
    )
    assert obj.entity_code == "TEST_HR_82"
    assert obj.value_amount == 82 * 100.5

def test_hr_entity_83_schema_validation():
    obj = HrSchemaEntity83Create(
        entity_code="TEST_HR_83",
        name="Test Entity 83",
        value_amount=83 * 100.5
    )
    assert obj.entity_code == "TEST_HR_83"
    assert obj.value_amount == 83 * 100.5

def test_hr_entity_84_schema_validation():
    obj = HrSchemaEntity84Create(
        entity_code="TEST_HR_84",
        name="Test Entity 84",
        value_amount=84 * 100.5
    )
    assert obj.entity_code == "TEST_HR_84"
    assert obj.value_amount == 84 * 100.5

def test_hr_entity_85_schema_validation():
    obj = HrSchemaEntity85Create(
        entity_code="TEST_HR_85",
        name="Test Entity 85",
        value_amount=85 * 100.5
    )
    assert obj.entity_code == "TEST_HR_85"
    assert obj.value_amount == 85 * 100.5

def test_hr_entity_86_schema_validation():
    obj = HrSchemaEntity86Create(
        entity_code="TEST_HR_86",
        name="Test Entity 86",
        value_amount=86 * 100.5
    )
    assert obj.entity_code == "TEST_HR_86"
    assert obj.value_amount == 86 * 100.5

def test_hr_entity_87_schema_validation():
    obj = HrSchemaEntity87Create(
        entity_code="TEST_HR_87",
        name="Test Entity 87",
        value_amount=87 * 100.5
    )
    assert obj.entity_code == "TEST_HR_87"
    assert obj.value_amount == 87 * 100.5

def test_hr_entity_88_schema_validation():
    obj = HrSchemaEntity88Create(
        entity_code="TEST_HR_88",
        name="Test Entity 88",
        value_amount=88 * 100.5
    )
    assert obj.entity_code == "TEST_HR_88"
    assert obj.value_amount == 88 * 100.5

def test_hr_entity_89_schema_validation():
    obj = HrSchemaEntity89Create(
        entity_code="TEST_HR_89",
        name="Test Entity 89",
        value_amount=89 * 100.5
    )
    assert obj.entity_code == "TEST_HR_89"
    assert obj.value_amount == 89 * 100.5

def test_hr_entity_90_schema_validation():
    obj = HrSchemaEntity90Create(
        entity_code="TEST_HR_90",
        name="Test Entity 90",
        value_amount=90 * 100.5
    )
    assert obj.entity_code == "TEST_HR_90"
    assert obj.value_amount == 90 * 100.5

def test_hr_entity_91_schema_validation():
    obj = HrSchemaEntity91Create(
        entity_code="TEST_HR_91",
        name="Test Entity 91",
        value_amount=91 * 100.5
    )
    assert obj.entity_code == "TEST_HR_91"
    assert obj.value_amount == 91 * 100.5

def test_hr_entity_92_schema_validation():
    obj = HrSchemaEntity92Create(
        entity_code="TEST_HR_92",
        name="Test Entity 92",
        value_amount=92 * 100.5
    )
    assert obj.entity_code == "TEST_HR_92"
    assert obj.value_amount == 92 * 100.5

def test_hr_entity_93_schema_validation():
    obj = HrSchemaEntity93Create(
        entity_code="TEST_HR_93",
        name="Test Entity 93",
        value_amount=93 * 100.5
    )
    assert obj.entity_code == "TEST_HR_93"
    assert obj.value_amount == 93 * 100.5

def test_hr_entity_94_schema_validation():
    obj = HrSchemaEntity94Create(
        entity_code="TEST_HR_94",
        name="Test Entity 94",
        value_amount=94 * 100.5
    )
    assert obj.entity_code == "TEST_HR_94"
    assert obj.value_amount == 94 * 100.5

def test_hr_entity_95_schema_validation():
    obj = HrSchemaEntity95Create(
        entity_code="TEST_HR_95",
        name="Test Entity 95",
        value_amount=95 * 100.5
    )
    assert obj.entity_code == "TEST_HR_95"
    assert obj.value_amount == 95 * 100.5

def test_hr_entity_96_schema_validation():
    obj = HrSchemaEntity96Create(
        entity_code="TEST_HR_96",
        name="Test Entity 96",
        value_amount=96 * 100.5
    )
    assert obj.entity_code == "TEST_HR_96"
    assert obj.value_amount == 96 * 100.5

def test_hr_entity_97_schema_validation():
    obj = HrSchemaEntity97Create(
        entity_code="TEST_HR_97",
        name="Test Entity 97",
        value_amount=97 * 100.5
    )
    assert obj.entity_code == "TEST_HR_97"
    assert obj.value_amount == 97 * 100.5

def test_hr_entity_98_schema_validation():
    obj = HrSchemaEntity98Create(
        entity_code="TEST_HR_98",
        name="Test Entity 98",
        value_amount=98 * 100.5
    )
    assert obj.entity_code == "TEST_HR_98"
    assert obj.value_amount == 98 * 100.5

def test_hr_entity_99_schema_validation():
    obj = HrSchemaEntity99Create(
        entity_code="TEST_HR_99",
        name="Test Entity 99",
        value_amount=99 * 100.5
    )
    assert obj.entity_code == "TEST_HR_99"
    assert obj.value_amount == 99 * 100.5

def test_hr_entity_100_schema_validation():
    obj = HrSchemaEntity100Create(
        entity_code="TEST_HR_100",
        name="Test Entity 100",
        value_amount=100 * 100.5
    )
    assert obj.entity_code == "TEST_HR_100"
    assert obj.value_amount == 100 * 100.5

def test_hr_entity_101_schema_validation():
    obj = HrSchemaEntity101Create(
        entity_code="TEST_HR_101",
        name="Test Entity 101",
        value_amount=101 * 100.5
    )
    assert obj.entity_code == "TEST_HR_101"
    assert obj.value_amount == 101 * 100.5

def test_hr_entity_102_schema_validation():
    obj = HrSchemaEntity102Create(
        entity_code="TEST_HR_102",
        name="Test Entity 102",
        value_amount=102 * 100.5
    )
    assert obj.entity_code == "TEST_HR_102"
    assert obj.value_amount == 102 * 100.5

def test_hr_entity_103_schema_validation():
    obj = HrSchemaEntity103Create(
        entity_code="TEST_HR_103",
        name="Test Entity 103",
        value_amount=103 * 100.5
    )
    assert obj.entity_code == "TEST_HR_103"
    assert obj.value_amount == 103 * 100.5

def test_hr_entity_104_schema_validation():
    obj = HrSchemaEntity104Create(
        entity_code="TEST_HR_104",
        name="Test Entity 104",
        value_amount=104 * 100.5
    )
    assert obj.entity_code == "TEST_HR_104"
    assert obj.value_amount == 104 * 100.5

def test_hr_entity_105_schema_validation():
    obj = HrSchemaEntity105Create(
        entity_code="TEST_HR_105",
        name="Test Entity 105",
        value_amount=105 * 100.5
    )
    assert obj.entity_code == "TEST_HR_105"
    assert obj.value_amount == 105 * 100.5

def test_hr_entity_106_schema_validation():
    obj = HrSchemaEntity106Create(
        entity_code="TEST_HR_106",
        name="Test Entity 106",
        value_amount=106 * 100.5
    )
    assert obj.entity_code == "TEST_HR_106"
    assert obj.value_amount == 106 * 100.5

def test_hr_entity_107_schema_validation():
    obj = HrSchemaEntity107Create(
        entity_code="TEST_HR_107",
        name="Test Entity 107",
        value_amount=107 * 100.5
    )
    assert obj.entity_code == "TEST_HR_107"
    assert obj.value_amount == 107 * 100.5

def test_hr_entity_108_schema_validation():
    obj = HrSchemaEntity108Create(
        entity_code="TEST_HR_108",
        name="Test Entity 108",
        value_amount=108 * 100.5
    )
    assert obj.entity_code == "TEST_HR_108"
    assert obj.value_amount == 108 * 100.5

def test_hr_entity_109_schema_validation():
    obj = HrSchemaEntity109Create(
        entity_code="TEST_HR_109",
        name="Test Entity 109",
        value_amount=109 * 100.5
    )
    assert obj.entity_code == "TEST_HR_109"
    assert obj.value_amount == 109 * 100.5

def test_hr_entity_110_schema_validation():
    obj = HrSchemaEntity110Create(
        entity_code="TEST_HR_110",
        name="Test Entity 110",
        value_amount=110 * 100.5
    )
    assert obj.entity_code == "TEST_HR_110"
    assert obj.value_amount == 110 * 100.5

def test_hr_entity_111_schema_validation():
    obj = HrSchemaEntity111Create(
        entity_code="TEST_HR_111",
        name="Test Entity 111",
        value_amount=111 * 100.5
    )
    assert obj.entity_code == "TEST_HR_111"
    assert obj.value_amount == 111 * 100.5

def test_hr_entity_112_schema_validation():
    obj = HrSchemaEntity112Create(
        entity_code="TEST_HR_112",
        name="Test Entity 112",
        value_amount=112 * 100.5
    )
    assert obj.entity_code == "TEST_HR_112"
    assert obj.value_amount == 112 * 100.5

def test_hr_entity_113_schema_validation():
    obj = HrSchemaEntity113Create(
        entity_code="TEST_HR_113",
        name="Test Entity 113",
        value_amount=113 * 100.5
    )
    assert obj.entity_code == "TEST_HR_113"
    assert obj.value_amount == 113 * 100.5

def test_hr_entity_114_schema_validation():
    obj = HrSchemaEntity114Create(
        entity_code="TEST_HR_114",
        name="Test Entity 114",
        value_amount=114 * 100.5
    )
    assert obj.entity_code == "TEST_HR_114"
    assert obj.value_amount == 114 * 100.5

def test_hr_entity_115_schema_validation():
    obj = HrSchemaEntity115Create(
        entity_code="TEST_HR_115",
        name="Test Entity 115",
        value_amount=115 * 100.5
    )
    assert obj.entity_code == "TEST_HR_115"
    assert obj.value_amount == 115 * 100.5

def test_hr_entity_116_schema_validation():
    obj = HrSchemaEntity116Create(
        entity_code="TEST_HR_116",
        name="Test Entity 116",
        value_amount=116 * 100.5
    )
    assert obj.entity_code == "TEST_HR_116"
    assert obj.value_amount == 116 * 100.5

def test_hr_entity_117_schema_validation():
    obj = HrSchemaEntity117Create(
        entity_code="TEST_HR_117",
        name="Test Entity 117",
        value_amount=117 * 100.5
    )
    assert obj.entity_code == "TEST_HR_117"
    assert obj.value_amount == 117 * 100.5

def test_hr_entity_118_schema_validation():
    obj = HrSchemaEntity118Create(
        entity_code="TEST_HR_118",
        name="Test Entity 118",
        value_amount=118 * 100.5
    )
    assert obj.entity_code == "TEST_HR_118"
    assert obj.value_amount == 118 * 100.5

def test_hr_entity_119_schema_validation():
    obj = HrSchemaEntity119Create(
        entity_code="TEST_HR_119",
        name="Test Entity 119",
        value_amount=119 * 100.5
    )
    assert obj.entity_code == "TEST_HR_119"
    assert obj.value_amount == 119 * 100.5

def test_hr_entity_120_schema_validation():
    obj = HrSchemaEntity120Create(
        entity_code="TEST_HR_120",
        name="Test Entity 120",
        value_amount=120 * 100.5
    )
    assert obj.entity_code == "TEST_HR_120"
    assert obj.value_amount == 120 * 100.5

def test_hr_entity_121_schema_validation():
    obj = HrSchemaEntity121Create(
        entity_code="TEST_HR_121",
        name="Test Entity 121",
        value_amount=121 * 100.5
    )
    assert obj.entity_code == "TEST_HR_121"
    assert obj.value_amount == 121 * 100.5

def test_hr_entity_122_schema_validation():
    obj = HrSchemaEntity122Create(
        entity_code="TEST_HR_122",
        name="Test Entity 122",
        value_amount=122 * 100.5
    )
    assert obj.entity_code == "TEST_HR_122"
    assert obj.value_amount == 122 * 100.5

def test_hr_entity_123_schema_validation():
    obj = HrSchemaEntity123Create(
        entity_code="TEST_HR_123",
        name="Test Entity 123",
        value_amount=123 * 100.5
    )
    assert obj.entity_code == "TEST_HR_123"
    assert obj.value_amount == 123 * 100.5

def test_hr_entity_124_schema_validation():
    obj = HrSchemaEntity124Create(
        entity_code="TEST_HR_124",
        name="Test Entity 124",
        value_amount=124 * 100.5
    )
    assert obj.entity_code == "TEST_HR_124"
    assert obj.value_amount == 124 * 100.5

def test_hr_entity_125_schema_validation():
    obj = HrSchemaEntity125Create(
        entity_code="TEST_HR_125",
        name="Test Entity 125",
        value_amount=125 * 100.5
    )
    assert obj.entity_code == "TEST_HR_125"
    assert obj.value_amount == 125 * 100.5

def test_hr_entity_126_schema_validation():
    obj = HrSchemaEntity126Create(
        entity_code="TEST_HR_126",
        name="Test Entity 126",
        value_amount=126 * 100.5
    )
    assert obj.entity_code == "TEST_HR_126"
    assert obj.value_amount == 126 * 100.5

def test_hr_entity_127_schema_validation():
    obj = HrSchemaEntity127Create(
        entity_code="TEST_HR_127",
        name="Test Entity 127",
        value_amount=127 * 100.5
    )
    assert obj.entity_code == "TEST_HR_127"
    assert obj.value_amount == 127 * 100.5

def test_hr_entity_128_schema_validation():
    obj = HrSchemaEntity128Create(
        entity_code="TEST_HR_128",
        name="Test Entity 128",
        value_amount=128 * 100.5
    )
    assert obj.entity_code == "TEST_HR_128"
    assert obj.value_amount == 128 * 100.5

def test_hr_entity_129_schema_validation():
    obj = HrSchemaEntity129Create(
        entity_code="TEST_HR_129",
        name="Test Entity 129",
        value_amount=129 * 100.5
    )
    assert obj.entity_code == "TEST_HR_129"
    assert obj.value_amount == 129 * 100.5

def test_hr_entity_130_schema_validation():
    obj = HrSchemaEntity130Create(
        entity_code="TEST_HR_130",
        name="Test Entity 130",
        value_amount=130 * 100.5
    )
    assert obj.entity_code == "TEST_HR_130"
    assert obj.value_amount == 130 * 100.5

def test_hr_entity_131_schema_validation():
    obj = HrSchemaEntity131Create(
        entity_code="TEST_HR_131",
        name="Test Entity 131",
        value_amount=131 * 100.5
    )
    assert obj.entity_code == "TEST_HR_131"
    assert obj.value_amount == 131 * 100.5

def test_hr_entity_132_schema_validation():
    obj = HrSchemaEntity132Create(
        entity_code="TEST_HR_132",
        name="Test Entity 132",
        value_amount=132 * 100.5
    )
    assert obj.entity_code == "TEST_HR_132"
    assert obj.value_amount == 132 * 100.5

def test_hr_entity_133_schema_validation():
    obj = HrSchemaEntity133Create(
        entity_code="TEST_HR_133",
        name="Test Entity 133",
        value_amount=133 * 100.5
    )
    assert obj.entity_code == "TEST_HR_133"
    assert obj.value_amount == 133 * 100.5

def test_hr_entity_134_schema_validation():
    obj = HrSchemaEntity134Create(
        entity_code="TEST_HR_134",
        name="Test Entity 134",
        value_amount=134 * 100.5
    )
    assert obj.entity_code == "TEST_HR_134"
    assert obj.value_amount == 134 * 100.5

def test_hr_entity_135_schema_validation():
    obj = HrSchemaEntity135Create(
        entity_code="TEST_HR_135",
        name="Test Entity 135",
        value_amount=135 * 100.5
    )
    assert obj.entity_code == "TEST_HR_135"
    assert obj.value_amount == 135 * 100.5

def test_hr_entity_136_schema_validation():
    obj = HrSchemaEntity136Create(
        entity_code="TEST_HR_136",
        name="Test Entity 136",
        value_amount=136 * 100.5
    )
    assert obj.entity_code == "TEST_HR_136"
    assert obj.value_amount == 136 * 100.5

def test_hr_entity_137_schema_validation():
    obj = HrSchemaEntity137Create(
        entity_code="TEST_HR_137",
        name="Test Entity 137",
        value_amount=137 * 100.5
    )
    assert obj.entity_code == "TEST_HR_137"
    assert obj.value_amount == 137 * 100.5

def test_hr_entity_138_schema_validation():
    obj = HrSchemaEntity138Create(
        entity_code="TEST_HR_138",
        name="Test Entity 138",
        value_amount=138 * 100.5
    )
    assert obj.entity_code == "TEST_HR_138"
    assert obj.value_amount == 138 * 100.5

def test_hr_entity_139_schema_validation():
    obj = HrSchemaEntity139Create(
        entity_code="TEST_HR_139",
        name="Test Entity 139",
        value_amount=139 * 100.5
    )
    assert obj.entity_code == "TEST_HR_139"
    assert obj.value_amount == 139 * 100.5

def test_hr_entity_140_schema_validation():
    obj = HrSchemaEntity140Create(
        entity_code="TEST_HR_140",
        name="Test Entity 140",
        value_amount=140 * 100.5
    )
    assert obj.entity_code == "TEST_HR_140"
    assert obj.value_amount == 140 * 100.5

def test_hr_entity_141_schema_validation():
    obj = HrSchemaEntity141Create(
        entity_code="TEST_HR_141",
        name="Test Entity 141",
        value_amount=141 * 100.5
    )
    assert obj.entity_code == "TEST_HR_141"
    assert obj.value_amount == 141 * 100.5

def test_hr_entity_142_schema_validation():
    obj = HrSchemaEntity142Create(
        entity_code="TEST_HR_142",
        name="Test Entity 142",
        value_amount=142 * 100.5
    )
    assert obj.entity_code == "TEST_HR_142"
    assert obj.value_amount == 142 * 100.5

def test_hr_entity_143_schema_validation():
    obj = HrSchemaEntity143Create(
        entity_code="TEST_HR_143",
        name="Test Entity 143",
        value_amount=143 * 100.5
    )
    assert obj.entity_code == "TEST_HR_143"
    assert obj.value_amount == 143 * 100.5

def test_hr_entity_144_schema_validation():
    obj = HrSchemaEntity144Create(
        entity_code="TEST_HR_144",
        name="Test Entity 144",
        value_amount=144 * 100.5
    )
    assert obj.entity_code == "TEST_HR_144"
    assert obj.value_amount == 144 * 100.5

def test_hr_entity_145_schema_validation():
    obj = HrSchemaEntity145Create(
        entity_code="TEST_HR_145",
        name="Test Entity 145",
        value_amount=145 * 100.5
    )
    assert obj.entity_code == "TEST_HR_145"
    assert obj.value_amount == 145 * 100.5

def test_hr_entity_146_schema_validation():
    obj = HrSchemaEntity146Create(
        entity_code="TEST_HR_146",
        name="Test Entity 146",
        value_amount=146 * 100.5
    )
    assert obj.entity_code == "TEST_HR_146"
    assert obj.value_amount == 146 * 100.5

def test_hr_entity_147_schema_validation():
    obj = HrSchemaEntity147Create(
        entity_code="TEST_HR_147",
        name="Test Entity 147",
        value_amount=147 * 100.5
    )
    assert obj.entity_code == "TEST_HR_147"
    assert obj.value_amount == 147 * 100.5

def test_hr_entity_148_schema_validation():
    obj = HrSchemaEntity148Create(
        entity_code="TEST_HR_148",
        name="Test Entity 148",
        value_amount=148 * 100.5
    )
    assert obj.entity_code == "TEST_HR_148"
    assert obj.value_amount == 148 * 100.5

def test_hr_entity_149_schema_validation():
    obj = HrSchemaEntity149Create(
        entity_code="TEST_HR_149",
        name="Test Entity 149",
        value_amount=149 * 100.5
    )
    assert obj.entity_code == "TEST_HR_149"
    assert obj.value_amount == 149 * 100.5

def test_hr_entity_150_schema_validation():
    obj = HrSchemaEntity150Create(
        entity_code="TEST_HR_150",
        name="Test Entity 150",
        value_amount=150 * 100.5
    )
    assert obj.entity_code == "TEST_HR_150"
    assert obj.value_amount == 150 * 100.5

def test_hr_entity_151_schema_validation():
    obj = HrSchemaEntity151Create(
        entity_code="TEST_HR_151",
        name="Test Entity 151",
        value_amount=151 * 100.5
    )
    assert obj.entity_code == "TEST_HR_151"
    assert obj.value_amount == 151 * 100.5

def test_hr_entity_152_schema_validation():
    obj = HrSchemaEntity152Create(
        entity_code="TEST_HR_152",
        name="Test Entity 152",
        value_amount=152 * 100.5
    )
    assert obj.entity_code == "TEST_HR_152"
    assert obj.value_amount == 152 * 100.5

def test_hr_entity_153_schema_validation():
    obj = HrSchemaEntity153Create(
        entity_code="TEST_HR_153",
        name="Test Entity 153",
        value_amount=153 * 100.5
    )
    assert obj.entity_code == "TEST_HR_153"
    assert obj.value_amount == 153 * 100.5

def test_hr_entity_154_schema_validation():
    obj = HrSchemaEntity154Create(
        entity_code="TEST_HR_154",
        name="Test Entity 154",
        value_amount=154 * 100.5
    )
    assert obj.entity_code == "TEST_HR_154"
    assert obj.value_amount == 154 * 100.5

def test_hr_entity_155_schema_validation():
    obj = HrSchemaEntity155Create(
        entity_code="TEST_HR_155",
        name="Test Entity 155",
        value_amount=155 * 100.5
    )
    assert obj.entity_code == "TEST_HR_155"
    assert obj.value_amount == 155 * 100.5

def test_hr_entity_156_schema_validation():
    obj = HrSchemaEntity156Create(
        entity_code="TEST_HR_156",
        name="Test Entity 156",
        value_amount=156 * 100.5
    )
    assert obj.entity_code == "TEST_HR_156"
    assert obj.value_amount == 156 * 100.5

def test_hr_entity_157_schema_validation():
    obj = HrSchemaEntity157Create(
        entity_code="TEST_HR_157",
        name="Test Entity 157",
        value_amount=157 * 100.5
    )
    assert obj.entity_code == "TEST_HR_157"
    assert obj.value_amount == 157 * 100.5

def test_hr_entity_158_schema_validation():
    obj = HrSchemaEntity158Create(
        entity_code="TEST_HR_158",
        name="Test Entity 158",
        value_amount=158 * 100.5
    )
    assert obj.entity_code == "TEST_HR_158"
    assert obj.value_amount == 158 * 100.5

def test_hr_entity_159_schema_validation():
    obj = HrSchemaEntity159Create(
        entity_code="TEST_HR_159",
        name="Test Entity 159",
        value_amount=159 * 100.5
    )
    assert obj.entity_code == "TEST_HR_159"
    assert obj.value_amount == 159 * 100.5

def test_hr_entity_160_schema_validation():
    obj = HrSchemaEntity160Create(
        entity_code="TEST_HR_160",
        name="Test Entity 160",
        value_amount=160 * 100.5
    )
    assert obj.entity_code == "TEST_HR_160"
    assert obj.value_amount == 160 * 100.5

def test_hr_entity_161_schema_validation():
    obj = HrSchemaEntity161Create(
        entity_code="TEST_HR_161",
        name="Test Entity 161",
        value_amount=161 * 100.5
    )
    assert obj.entity_code == "TEST_HR_161"
    assert obj.value_amount == 161 * 100.5

def test_hr_entity_162_schema_validation():
    obj = HrSchemaEntity162Create(
        entity_code="TEST_HR_162",
        name="Test Entity 162",
        value_amount=162 * 100.5
    )
    assert obj.entity_code == "TEST_HR_162"
    assert obj.value_amount == 162 * 100.5

def test_hr_entity_163_schema_validation():
    obj = HrSchemaEntity163Create(
        entity_code="TEST_HR_163",
        name="Test Entity 163",
        value_amount=163 * 100.5
    )
    assert obj.entity_code == "TEST_HR_163"
    assert obj.value_amount == 163 * 100.5

def test_hr_entity_164_schema_validation():
    obj = HrSchemaEntity164Create(
        entity_code="TEST_HR_164",
        name="Test Entity 164",
        value_amount=164 * 100.5
    )
    assert obj.entity_code == "TEST_HR_164"
    assert obj.value_amount == 164 * 100.5

def test_hr_entity_165_schema_validation():
    obj = HrSchemaEntity165Create(
        entity_code="TEST_HR_165",
        name="Test Entity 165",
        value_amount=165 * 100.5
    )
    assert obj.entity_code == "TEST_HR_165"
    assert obj.value_amount == 165 * 100.5

def test_hr_entity_166_schema_validation():
    obj = HrSchemaEntity166Create(
        entity_code="TEST_HR_166",
        name="Test Entity 166",
        value_amount=166 * 100.5
    )
    assert obj.entity_code == "TEST_HR_166"
    assert obj.value_amount == 166 * 100.5

def test_hr_entity_167_schema_validation():
    obj = HrSchemaEntity167Create(
        entity_code="TEST_HR_167",
        name="Test Entity 167",
        value_amount=167 * 100.5
    )
    assert obj.entity_code == "TEST_HR_167"
    assert obj.value_amount == 167 * 100.5

def test_hr_entity_168_schema_validation():
    obj = HrSchemaEntity168Create(
        entity_code="TEST_HR_168",
        name="Test Entity 168",
        value_amount=168 * 100.5
    )
    assert obj.entity_code == "TEST_HR_168"
    assert obj.value_amount == 168 * 100.5

def test_hr_entity_169_schema_validation():
    obj = HrSchemaEntity169Create(
        entity_code="TEST_HR_169",
        name="Test Entity 169",
        value_amount=169 * 100.5
    )
    assert obj.entity_code == "TEST_HR_169"
    assert obj.value_amount == 169 * 100.5

def test_hr_entity_170_schema_validation():
    obj = HrSchemaEntity170Create(
        entity_code="TEST_HR_170",
        name="Test Entity 170",
        value_amount=170 * 100.5
    )
    assert obj.entity_code == "TEST_HR_170"
    assert obj.value_amount == 170 * 100.5

def test_hr_entity_171_schema_validation():
    obj = HrSchemaEntity171Create(
        entity_code="TEST_HR_171",
        name="Test Entity 171",
        value_amount=171 * 100.5
    )
    assert obj.entity_code == "TEST_HR_171"
    assert obj.value_amount == 171 * 100.5

def test_hr_entity_172_schema_validation():
    obj = HrSchemaEntity172Create(
        entity_code="TEST_HR_172",
        name="Test Entity 172",
        value_amount=172 * 100.5
    )
    assert obj.entity_code == "TEST_HR_172"
    assert obj.value_amount == 172 * 100.5

def test_hr_entity_173_schema_validation():
    obj = HrSchemaEntity173Create(
        entity_code="TEST_HR_173",
        name="Test Entity 173",
        value_amount=173 * 100.5
    )
    assert obj.entity_code == "TEST_HR_173"
    assert obj.value_amount == 173 * 100.5

def test_hr_entity_174_schema_validation():
    obj = HrSchemaEntity174Create(
        entity_code="TEST_HR_174",
        name="Test Entity 174",
        value_amount=174 * 100.5
    )
    assert obj.entity_code == "TEST_HR_174"
    assert obj.value_amount == 174 * 100.5

def test_hr_entity_175_schema_validation():
    obj = HrSchemaEntity175Create(
        entity_code="TEST_HR_175",
        name="Test Entity 175",
        value_amount=175 * 100.5
    )
    assert obj.entity_code == "TEST_HR_175"
    assert obj.value_amount == 175 * 100.5

def test_hr_entity_176_schema_validation():
    obj = HrSchemaEntity176Create(
        entity_code="TEST_HR_176",
        name="Test Entity 176",
        value_amount=176 * 100.5
    )
    assert obj.entity_code == "TEST_HR_176"
    assert obj.value_amount == 176 * 100.5

def test_hr_entity_177_schema_validation():
    obj = HrSchemaEntity177Create(
        entity_code="TEST_HR_177",
        name="Test Entity 177",
        value_amount=177 * 100.5
    )
    assert obj.entity_code == "TEST_HR_177"
    assert obj.value_amount == 177 * 100.5

def test_hr_entity_178_schema_validation():
    obj = HrSchemaEntity178Create(
        entity_code="TEST_HR_178",
        name="Test Entity 178",
        value_amount=178 * 100.5
    )
    assert obj.entity_code == "TEST_HR_178"
    assert obj.value_amount == 178 * 100.5

def test_hr_entity_179_schema_validation():
    obj = HrSchemaEntity179Create(
        entity_code="TEST_HR_179",
        name="Test Entity 179",
        value_amount=179 * 100.5
    )
    assert obj.entity_code == "TEST_HR_179"
    assert obj.value_amount == 179 * 100.5

def test_hr_entity_180_schema_validation():
    obj = HrSchemaEntity180Create(
        entity_code="TEST_HR_180",
        name="Test Entity 180",
        value_amount=180 * 100.5
    )
    assert obj.entity_code == "TEST_HR_180"
    assert obj.value_amount == 180 * 100.5

def test_hr_entity_181_schema_validation():
    obj = HrSchemaEntity181Create(
        entity_code="TEST_HR_181",
        name="Test Entity 181",
        value_amount=181 * 100.5
    )
    assert obj.entity_code == "TEST_HR_181"
    assert obj.value_amount == 181 * 100.5

def test_hr_entity_182_schema_validation():
    obj = HrSchemaEntity182Create(
        entity_code="TEST_HR_182",
        name="Test Entity 182",
        value_amount=182 * 100.5
    )
    assert obj.entity_code == "TEST_HR_182"
    assert obj.value_amount == 182 * 100.5

def test_hr_entity_183_schema_validation():
    obj = HrSchemaEntity183Create(
        entity_code="TEST_HR_183",
        name="Test Entity 183",
        value_amount=183 * 100.5
    )
    assert obj.entity_code == "TEST_HR_183"
    assert obj.value_amount == 183 * 100.5

def test_hr_entity_184_schema_validation():
    obj = HrSchemaEntity184Create(
        entity_code="TEST_HR_184",
        name="Test Entity 184",
        value_amount=184 * 100.5
    )
    assert obj.entity_code == "TEST_HR_184"
    assert obj.value_amount == 184 * 100.5

def test_hr_entity_185_schema_validation():
    obj = HrSchemaEntity185Create(
        entity_code="TEST_HR_185",
        name="Test Entity 185",
        value_amount=185 * 100.5
    )
    assert obj.entity_code == "TEST_HR_185"
    assert obj.value_amount == 185 * 100.5

def test_hr_entity_186_schema_validation():
    obj = HrSchemaEntity186Create(
        entity_code="TEST_HR_186",
        name="Test Entity 186",
        value_amount=186 * 100.5
    )
    assert obj.entity_code == "TEST_HR_186"
    assert obj.value_amount == 186 * 100.5

def test_hr_entity_187_schema_validation():
    obj = HrSchemaEntity187Create(
        entity_code="TEST_HR_187",
        name="Test Entity 187",
        value_amount=187 * 100.5
    )
    assert obj.entity_code == "TEST_HR_187"
    assert obj.value_amount == 187 * 100.5

def test_hr_entity_188_schema_validation():
    obj = HrSchemaEntity188Create(
        entity_code="TEST_HR_188",
        name="Test Entity 188",
        value_amount=188 * 100.5
    )
    assert obj.entity_code == "TEST_HR_188"
    assert obj.value_amount == 188 * 100.5

def test_hr_entity_189_schema_validation():
    obj = HrSchemaEntity189Create(
        entity_code="TEST_HR_189",
        name="Test Entity 189",
        value_amount=189 * 100.5
    )
    assert obj.entity_code == "TEST_HR_189"
    assert obj.value_amount == 189 * 100.5

def test_hr_entity_190_schema_validation():
    obj = HrSchemaEntity190Create(
        entity_code="TEST_HR_190",
        name="Test Entity 190",
        value_amount=190 * 100.5
    )
    assert obj.entity_code == "TEST_HR_190"
    assert obj.value_amount == 190 * 100.5

def test_hr_entity_191_schema_validation():
    obj = HrSchemaEntity191Create(
        entity_code="TEST_HR_191",
        name="Test Entity 191",
        value_amount=191 * 100.5
    )
    assert obj.entity_code == "TEST_HR_191"
    assert obj.value_amount == 191 * 100.5

def test_hr_entity_192_schema_validation():
    obj = HrSchemaEntity192Create(
        entity_code="TEST_HR_192",
        name="Test Entity 192",
        value_amount=192 * 100.5
    )
    assert obj.entity_code == "TEST_HR_192"
    assert obj.value_amount == 192 * 100.5

def test_hr_entity_193_schema_validation():
    obj = HrSchemaEntity193Create(
        entity_code="TEST_HR_193",
        name="Test Entity 193",
        value_amount=193 * 100.5
    )
    assert obj.entity_code == "TEST_HR_193"
    assert obj.value_amount == 193 * 100.5

def test_hr_entity_194_schema_validation():
    obj = HrSchemaEntity194Create(
        entity_code="TEST_HR_194",
        name="Test Entity 194",
        value_amount=194 * 100.5
    )
    assert obj.entity_code == "TEST_HR_194"
    assert obj.value_amount == 194 * 100.5

def test_hr_entity_195_schema_validation():
    obj = HrSchemaEntity195Create(
        entity_code="TEST_HR_195",
        name="Test Entity 195",
        value_amount=195 * 100.5
    )
    assert obj.entity_code == "TEST_HR_195"
    assert obj.value_amount == 195 * 100.5

def test_hr_entity_196_schema_validation():
    obj = HrSchemaEntity196Create(
        entity_code="TEST_HR_196",
        name="Test Entity 196",
        value_amount=196 * 100.5
    )
    assert obj.entity_code == "TEST_HR_196"
    assert obj.value_amount == 196 * 100.5

def test_hr_entity_197_schema_validation():
    obj = HrSchemaEntity197Create(
        entity_code="TEST_HR_197",
        name="Test Entity 197",
        value_amount=197 * 100.5
    )
    assert obj.entity_code == "TEST_HR_197"
    assert obj.value_amount == 197 * 100.5

def test_hr_entity_198_schema_validation():
    obj = HrSchemaEntity198Create(
        entity_code="TEST_HR_198",
        name="Test Entity 198",
        value_amount=198 * 100.5
    )
    assert obj.entity_code == "TEST_HR_198"
    assert obj.value_amount == 198 * 100.5

def test_hr_entity_199_schema_validation():
    obj = HrSchemaEntity199Create(
        entity_code="TEST_HR_199",
        name="Test Entity 199",
        value_amount=199 * 100.5
    )
    assert obj.entity_code == "TEST_HR_199"
    assert obj.value_amount == 199 * 100.5

def test_hr_entity_200_schema_validation():
    obj = HrSchemaEntity200Create(
        entity_code="TEST_HR_200",
        name="Test Entity 200",
        value_amount=200 * 100.5
    )
    assert obj.entity_code == "TEST_HR_200"
    assert obj.value_amount == 200 * 100.5


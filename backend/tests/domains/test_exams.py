"""
Pytest suite for Examinations & Result Management
"""
import pytest
from app.domains.exams.schemas import *

def test_exams_entity_1_schema_validation():
    obj = ExamsSchemaEntity1Create(
        entity_code="TEST_EXAMS_1",
        name="Test Entity 1",
        value_amount=1 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_1"
    assert obj.value_amount == 1 * 100.5

def test_exams_entity_2_schema_validation():
    obj = ExamsSchemaEntity2Create(
        entity_code="TEST_EXAMS_2",
        name="Test Entity 2",
        value_amount=2 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_2"
    assert obj.value_amount == 2 * 100.5

def test_exams_entity_3_schema_validation():
    obj = ExamsSchemaEntity3Create(
        entity_code="TEST_EXAMS_3",
        name="Test Entity 3",
        value_amount=3 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_3"
    assert obj.value_amount == 3 * 100.5

def test_exams_entity_4_schema_validation():
    obj = ExamsSchemaEntity4Create(
        entity_code="TEST_EXAMS_4",
        name="Test Entity 4",
        value_amount=4 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_4"
    assert obj.value_amount == 4 * 100.5

def test_exams_entity_5_schema_validation():
    obj = ExamsSchemaEntity5Create(
        entity_code="TEST_EXAMS_5",
        name="Test Entity 5",
        value_amount=5 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_5"
    assert obj.value_amount == 5 * 100.5

def test_exams_entity_6_schema_validation():
    obj = ExamsSchemaEntity6Create(
        entity_code="TEST_EXAMS_6",
        name="Test Entity 6",
        value_amount=6 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_6"
    assert obj.value_amount == 6 * 100.5

def test_exams_entity_7_schema_validation():
    obj = ExamsSchemaEntity7Create(
        entity_code="TEST_EXAMS_7",
        name="Test Entity 7",
        value_amount=7 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_7"
    assert obj.value_amount == 7 * 100.5

def test_exams_entity_8_schema_validation():
    obj = ExamsSchemaEntity8Create(
        entity_code="TEST_EXAMS_8",
        name="Test Entity 8",
        value_amount=8 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_8"
    assert obj.value_amount == 8 * 100.5

def test_exams_entity_9_schema_validation():
    obj = ExamsSchemaEntity9Create(
        entity_code="TEST_EXAMS_9",
        name="Test Entity 9",
        value_amount=9 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_9"
    assert obj.value_amount == 9 * 100.5

def test_exams_entity_10_schema_validation():
    obj = ExamsSchemaEntity10Create(
        entity_code="TEST_EXAMS_10",
        name="Test Entity 10",
        value_amount=10 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_10"
    assert obj.value_amount == 10 * 100.5

def test_exams_entity_11_schema_validation():
    obj = ExamsSchemaEntity11Create(
        entity_code="TEST_EXAMS_11",
        name="Test Entity 11",
        value_amount=11 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_11"
    assert obj.value_amount == 11 * 100.5

def test_exams_entity_12_schema_validation():
    obj = ExamsSchemaEntity12Create(
        entity_code="TEST_EXAMS_12",
        name="Test Entity 12",
        value_amount=12 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_12"
    assert obj.value_amount == 12 * 100.5

def test_exams_entity_13_schema_validation():
    obj = ExamsSchemaEntity13Create(
        entity_code="TEST_EXAMS_13",
        name="Test Entity 13",
        value_amount=13 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_13"
    assert obj.value_amount == 13 * 100.5

def test_exams_entity_14_schema_validation():
    obj = ExamsSchemaEntity14Create(
        entity_code="TEST_EXAMS_14",
        name="Test Entity 14",
        value_amount=14 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_14"
    assert obj.value_amount == 14 * 100.5

def test_exams_entity_15_schema_validation():
    obj = ExamsSchemaEntity15Create(
        entity_code="TEST_EXAMS_15",
        name="Test Entity 15",
        value_amount=15 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_15"
    assert obj.value_amount == 15 * 100.5

def test_exams_entity_16_schema_validation():
    obj = ExamsSchemaEntity16Create(
        entity_code="TEST_EXAMS_16",
        name="Test Entity 16",
        value_amount=16 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_16"
    assert obj.value_amount == 16 * 100.5

def test_exams_entity_17_schema_validation():
    obj = ExamsSchemaEntity17Create(
        entity_code="TEST_EXAMS_17",
        name="Test Entity 17",
        value_amount=17 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_17"
    assert obj.value_amount == 17 * 100.5

def test_exams_entity_18_schema_validation():
    obj = ExamsSchemaEntity18Create(
        entity_code="TEST_EXAMS_18",
        name="Test Entity 18",
        value_amount=18 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_18"
    assert obj.value_amount == 18 * 100.5

def test_exams_entity_19_schema_validation():
    obj = ExamsSchemaEntity19Create(
        entity_code="TEST_EXAMS_19",
        name="Test Entity 19",
        value_amount=19 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_19"
    assert obj.value_amount == 19 * 100.5

def test_exams_entity_20_schema_validation():
    obj = ExamsSchemaEntity20Create(
        entity_code="TEST_EXAMS_20",
        name="Test Entity 20",
        value_amount=20 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_20"
    assert obj.value_amount == 20 * 100.5

def test_exams_entity_21_schema_validation():
    obj = ExamsSchemaEntity21Create(
        entity_code="TEST_EXAMS_21",
        name="Test Entity 21",
        value_amount=21 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_21"
    assert obj.value_amount == 21 * 100.5

def test_exams_entity_22_schema_validation():
    obj = ExamsSchemaEntity22Create(
        entity_code="TEST_EXAMS_22",
        name="Test Entity 22",
        value_amount=22 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_22"
    assert obj.value_amount == 22 * 100.5

def test_exams_entity_23_schema_validation():
    obj = ExamsSchemaEntity23Create(
        entity_code="TEST_EXAMS_23",
        name="Test Entity 23",
        value_amount=23 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_23"
    assert obj.value_amount == 23 * 100.5

def test_exams_entity_24_schema_validation():
    obj = ExamsSchemaEntity24Create(
        entity_code="TEST_EXAMS_24",
        name="Test Entity 24",
        value_amount=24 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_24"
    assert obj.value_amount == 24 * 100.5

def test_exams_entity_25_schema_validation():
    obj = ExamsSchemaEntity25Create(
        entity_code="TEST_EXAMS_25",
        name="Test Entity 25",
        value_amount=25 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_25"
    assert obj.value_amount == 25 * 100.5

def test_exams_entity_26_schema_validation():
    obj = ExamsSchemaEntity26Create(
        entity_code="TEST_EXAMS_26",
        name="Test Entity 26",
        value_amount=26 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_26"
    assert obj.value_amount == 26 * 100.5

def test_exams_entity_27_schema_validation():
    obj = ExamsSchemaEntity27Create(
        entity_code="TEST_EXAMS_27",
        name="Test Entity 27",
        value_amount=27 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_27"
    assert obj.value_amount == 27 * 100.5

def test_exams_entity_28_schema_validation():
    obj = ExamsSchemaEntity28Create(
        entity_code="TEST_EXAMS_28",
        name="Test Entity 28",
        value_amount=28 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_28"
    assert obj.value_amount == 28 * 100.5

def test_exams_entity_29_schema_validation():
    obj = ExamsSchemaEntity29Create(
        entity_code="TEST_EXAMS_29",
        name="Test Entity 29",
        value_amount=29 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_29"
    assert obj.value_amount == 29 * 100.5

def test_exams_entity_30_schema_validation():
    obj = ExamsSchemaEntity30Create(
        entity_code="TEST_EXAMS_30",
        name="Test Entity 30",
        value_amount=30 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_30"
    assert obj.value_amount == 30 * 100.5

def test_exams_entity_31_schema_validation():
    obj = ExamsSchemaEntity31Create(
        entity_code="TEST_EXAMS_31",
        name="Test Entity 31",
        value_amount=31 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_31"
    assert obj.value_amount == 31 * 100.5

def test_exams_entity_32_schema_validation():
    obj = ExamsSchemaEntity32Create(
        entity_code="TEST_EXAMS_32",
        name="Test Entity 32",
        value_amount=32 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_32"
    assert obj.value_amount == 32 * 100.5

def test_exams_entity_33_schema_validation():
    obj = ExamsSchemaEntity33Create(
        entity_code="TEST_EXAMS_33",
        name="Test Entity 33",
        value_amount=33 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_33"
    assert obj.value_amount == 33 * 100.5

def test_exams_entity_34_schema_validation():
    obj = ExamsSchemaEntity34Create(
        entity_code="TEST_EXAMS_34",
        name="Test Entity 34",
        value_amount=34 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_34"
    assert obj.value_amount == 34 * 100.5

def test_exams_entity_35_schema_validation():
    obj = ExamsSchemaEntity35Create(
        entity_code="TEST_EXAMS_35",
        name="Test Entity 35",
        value_amount=35 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_35"
    assert obj.value_amount == 35 * 100.5

def test_exams_entity_36_schema_validation():
    obj = ExamsSchemaEntity36Create(
        entity_code="TEST_EXAMS_36",
        name="Test Entity 36",
        value_amount=36 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_36"
    assert obj.value_amount == 36 * 100.5

def test_exams_entity_37_schema_validation():
    obj = ExamsSchemaEntity37Create(
        entity_code="TEST_EXAMS_37",
        name="Test Entity 37",
        value_amount=37 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_37"
    assert obj.value_amount == 37 * 100.5

def test_exams_entity_38_schema_validation():
    obj = ExamsSchemaEntity38Create(
        entity_code="TEST_EXAMS_38",
        name="Test Entity 38",
        value_amount=38 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_38"
    assert obj.value_amount == 38 * 100.5

def test_exams_entity_39_schema_validation():
    obj = ExamsSchemaEntity39Create(
        entity_code="TEST_EXAMS_39",
        name="Test Entity 39",
        value_amount=39 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_39"
    assert obj.value_amount == 39 * 100.5

def test_exams_entity_40_schema_validation():
    obj = ExamsSchemaEntity40Create(
        entity_code="TEST_EXAMS_40",
        name="Test Entity 40",
        value_amount=40 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_40"
    assert obj.value_amount == 40 * 100.5

def test_exams_entity_41_schema_validation():
    obj = ExamsSchemaEntity41Create(
        entity_code="TEST_EXAMS_41",
        name="Test Entity 41",
        value_amount=41 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_41"
    assert obj.value_amount == 41 * 100.5

def test_exams_entity_42_schema_validation():
    obj = ExamsSchemaEntity42Create(
        entity_code="TEST_EXAMS_42",
        name="Test Entity 42",
        value_amount=42 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_42"
    assert obj.value_amount == 42 * 100.5

def test_exams_entity_43_schema_validation():
    obj = ExamsSchemaEntity43Create(
        entity_code="TEST_EXAMS_43",
        name="Test Entity 43",
        value_amount=43 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_43"
    assert obj.value_amount == 43 * 100.5

def test_exams_entity_44_schema_validation():
    obj = ExamsSchemaEntity44Create(
        entity_code="TEST_EXAMS_44",
        name="Test Entity 44",
        value_amount=44 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_44"
    assert obj.value_amount == 44 * 100.5

def test_exams_entity_45_schema_validation():
    obj = ExamsSchemaEntity45Create(
        entity_code="TEST_EXAMS_45",
        name="Test Entity 45",
        value_amount=45 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_45"
    assert obj.value_amount == 45 * 100.5

def test_exams_entity_46_schema_validation():
    obj = ExamsSchemaEntity46Create(
        entity_code="TEST_EXAMS_46",
        name="Test Entity 46",
        value_amount=46 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_46"
    assert obj.value_amount == 46 * 100.5

def test_exams_entity_47_schema_validation():
    obj = ExamsSchemaEntity47Create(
        entity_code="TEST_EXAMS_47",
        name="Test Entity 47",
        value_amount=47 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_47"
    assert obj.value_amount == 47 * 100.5

def test_exams_entity_48_schema_validation():
    obj = ExamsSchemaEntity48Create(
        entity_code="TEST_EXAMS_48",
        name="Test Entity 48",
        value_amount=48 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_48"
    assert obj.value_amount == 48 * 100.5

def test_exams_entity_49_schema_validation():
    obj = ExamsSchemaEntity49Create(
        entity_code="TEST_EXAMS_49",
        name="Test Entity 49",
        value_amount=49 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_49"
    assert obj.value_amount == 49 * 100.5

def test_exams_entity_50_schema_validation():
    obj = ExamsSchemaEntity50Create(
        entity_code="TEST_EXAMS_50",
        name="Test Entity 50",
        value_amount=50 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_50"
    assert obj.value_amount == 50 * 100.5

def test_exams_entity_51_schema_validation():
    obj = ExamsSchemaEntity51Create(
        entity_code="TEST_EXAMS_51",
        name="Test Entity 51",
        value_amount=51 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_51"
    assert obj.value_amount == 51 * 100.5

def test_exams_entity_52_schema_validation():
    obj = ExamsSchemaEntity52Create(
        entity_code="TEST_EXAMS_52",
        name="Test Entity 52",
        value_amount=52 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_52"
    assert obj.value_amount == 52 * 100.5

def test_exams_entity_53_schema_validation():
    obj = ExamsSchemaEntity53Create(
        entity_code="TEST_EXAMS_53",
        name="Test Entity 53",
        value_amount=53 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_53"
    assert obj.value_amount == 53 * 100.5

def test_exams_entity_54_schema_validation():
    obj = ExamsSchemaEntity54Create(
        entity_code="TEST_EXAMS_54",
        name="Test Entity 54",
        value_amount=54 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_54"
    assert obj.value_amount == 54 * 100.5

def test_exams_entity_55_schema_validation():
    obj = ExamsSchemaEntity55Create(
        entity_code="TEST_EXAMS_55",
        name="Test Entity 55",
        value_amount=55 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_55"
    assert obj.value_amount == 55 * 100.5

def test_exams_entity_56_schema_validation():
    obj = ExamsSchemaEntity56Create(
        entity_code="TEST_EXAMS_56",
        name="Test Entity 56",
        value_amount=56 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_56"
    assert obj.value_amount == 56 * 100.5

def test_exams_entity_57_schema_validation():
    obj = ExamsSchemaEntity57Create(
        entity_code="TEST_EXAMS_57",
        name="Test Entity 57",
        value_amount=57 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_57"
    assert obj.value_amount == 57 * 100.5

def test_exams_entity_58_schema_validation():
    obj = ExamsSchemaEntity58Create(
        entity_code="TEST_EXAMS_58",
        name="Test Entity 58",
        value_amount=58 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_58"
    assert obj.value_amount == 58 * 100.5

def test_exams_entity_59_schema_validation():
    obj = ExamsSchemaEntity59Create(
        entity_code="TEST_EXAMS_59",
        name="Test Entity 59",
        value_amount=59 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_59"
    assert obj.value_amount == 59 * 100.5

def test_exams_entity_60_schema_validation():
    obj = ExamsSchemaEntity60Create(
        entity_code="TEST_EXAMS_60",
        name="Test Entity 60",
        value_amount=60 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_60"
    assert obj.value_amount == 60 * 100.5

def test_exams_entity_61_schema_validation():
    obj = ExamsSchemaEntity61Create(
        entity_code="TEST_EXAMS_61",
        name="Test Entity 61",
        value_amount=61 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_61"
    assert obj.value_amount == 61 * 100.5

def test_exams_entity_62_schema_validation():
    obj = ExamsSchemaEntity62Create(
        entity_code="TEST_EXAMS_62",
        name="Test Entity 62",
        value_amount=62 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_62"
    assert obj.value_amount == 62 * 100.5

def test_exams_entity_63_schema_validation():
    obj = ExamsSchemaEntity63Create(
        entity_code="TEST_EXAMS_63",
        name="Test Entity 63",
        value_amount=63 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_63"
    assert obj.value_amount == 63 * 100.5

def test_exams_entity_64_schema_validation():
    obj = ExamsSchemaEntity64Create(
        entity_code="TEST_EXAMS_64",
        name="Test Entity 64",
        value_amount=64 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_64"
    assert obj.value_amount == 64 * 100.5

def test_exams_entity_65_schema_validation():
    obj = ExamsSchemaEntity65Create(
        entity_code="TEST_EXAMS_65",
        name="Test Entity 65",
        value_amount=65 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_65"
    assert obj.value_amount == 65 * 100.5

def test_exams_entity_66_schema_validation():
    obj = ExamsSchemaEntity66Create(
        entity_code="TEST_EXAMS_66",
        name="Test Entity 66",
        value_amount=66 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_66"
    assert obj.value_amount == 66 * 100.5

def test_exams_entity_67_schema_validation():
    obj = ExamsSchemaEntity67Create(
        entity_code="TEST_EXAMS_67",
        name="Test Entity 67",
        value_amount=67 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_67"
    assert obj.value_amount == 67 * 100.5

def test_exams_entity_68_schema_validation():
    obj = ExamsSchemaEntity68Create(
        entity_code="TEST_EXAMS_68",
        name="Test Entity 68",
        value_amount=68 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_68"
    assert obj.value_amount == 68 * 100.5

def test_exams_entity_69_schema_validation():
    obj = ExamsSchemaEntity69Create(
        entity_code="TEST_EXAMS_69",
        name="Test Entity 69",
        value_amount=69 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_69"
    assert obj.value_amount == 69 * 100.5

def test_exams_entity_70_schema_validation():
    obj = ExamsSchemaEntity70Create(
        entity_code="TEST_EXAMS_70",
        name="Test Entity 70",
        value_amount=70 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_70"
    assert obj.value_amount == 70 * 100.5

def test_exams_entity_71_schema_validation():
    obj = ExamsSchemaEntity71Create(
        entity_code="TEST_EXAMS_71",
        name="Test Entity 71",
        value_amount=71 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_71"
    assert obj.value_amount == 71 * 100.5

def test_exams_entity_72_schema_validation():
    obj = ExamsSchemaEntity72Create(
        entity_code="TEST_EXAMS_72",
        name="Test Entity 72",
        value_amount=72 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_72"
    assert obj.value_amount == 72 * 100.5

def test_exams_entity_73_schema_validation():
    obj = ExamsSchemaEntity73Create(
        entity_code="TEST_EXAMS_73",
        name="Test Entity 73",
        value_amount=73 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_73"
    assert obj.value_amount == 73 * 100.5

def test_exams_entity_74_schema_validation():
    obj = ExamsSchemaEntity74Create(
        entity_code="TEST_EXAMS_74",
        name="Test Entity 74",
        value_amount=74 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_74"
    assert obj.value_amount == 74 * 100.5

def test_exams_entity_75_schema_validation():
    obj = ExamsSchemaEntity75Create(
        entity_code="TEST_EXAMS_75",
        name="Test Entity 75",
        value_amount=75 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_75"
    assert obj.value_amount == 75 * 100.5

def test_exams_entity_76_schema_validation():
    obj = ExamsSchemaEntity76Create(
        entity_code="TEST_EXAMS_76",
        name="Test Entity 76",
        value_amount=76 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_76"
    assert obj.value_amount == 76 * 100.5

def test_exams_entity_77_schema_validation():
    obj = ExamsSchemaEntity77Create(
        entity_code="TEST_EXAMS_77",
        name="Test Entity 77",
        value_amount=77 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_77"
    assert obj.value_amount == 77 * 100.5

def test_exams_entity_78_schema_validation():
    obj = ExamsSchemaEntity78Create(
        entity_code="TEST_EXAMS_78",
        name="Test Entity 78",
        value_amount=78 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_78"
    assert obj.value_amount == 78 * 100.5

def test_exams_entity_79_schema_validation():
    obj = ExamsSchemaEntity79Create(
        entity_code="TEST_EXAMS_79",
        name="Test Entity 79",
        value_amount=79 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_79"
    assert obj.value_amount == 79 * 100.5

def test_exams_entity_80_schema_validation():
    obj = ExamsSchemaEntity80Create(
        entity_code="TEST_EXAMS_80",
        name="Test Entity 80",
        value_amount=80 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_80"
    assert obj.value_amount == 80 * 100.5

def test_exams_entity_81_schema_validation():
    obj = ExamsSchemaEntity81Create(
        entity_code="TEST_EXAMS_81",
        name="Test Entity 81",
        value_amount=81 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_81"
    assert obj.value_amount == 81 * 100.5

def test_exams_entity_82_schema_validation():
    obj = ExamsSchemaEntity82Create(
        entity_code="TEST_EXAMS_82",
        name="Test Entity 82",
        value_amount=82 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_82"
    assert obj.value_amount == 82 * 100.5

def test_exams_entity_83_schema_validation():
    obj = ExamsSchemaEntity83Create(
        entity_code="TEST_EXAMS_83",
        name="Test Entity 83",
        value_amount=83 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_83"
    assert obj.value_amount == 83 * 100.5

def test_exams_entity_84_schema_validation():
    obj = ExamsSchemaEntity84Create(
        entity_code="TEST_EXAMS_84",
        name="Test Entity 84",
        value_amount=84 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_84"
    assert obj.value_amount == 84 * 100.5

def test_exams_entity_85_schema_validation():
    obj = ExamsSchemaEntity85Create(
        entity_code="TEST_EXAMS_85",
        name="Test Entity 85",
        value_amount=85 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_85"
    assert obj.value_amount == 85 * 100.5

def test_exams_entity_86_schema_validation():
    obj = ExamsSchemaEntity86Create(
        entity_code="TEST_EXAMS_86",
        name="Test Entity 86",
        value_amount=86 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_86"
    assert obj.value_amount == 86 * 100.5

def test_exams_entity_87_schema_validation():
    obj = ExamsSchemaEntity87Create(
        entity_code="TEST_EXAMS_87",
        name="Test Entity 87",
        value_amount=87 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_87"
    assert obj.value_amount == 87 * 100.5

def test_exams_entity_88_schema_validation():
    obj = ExamsSchemaEntity88Create(
        entity_code="TEST_EXAMS_88",
        name="Test Entity 88",
        value_amount=88 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_88"
    assert obj.value_amount == 88 * 100.5

def test_exams_entity_89_schema_validation():
    obj = ExamsSchemaEntity89Create(
        entity_code="TEST_EXAMS_89",
        name="Test Entity 89",
        value_amount=89 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_89"
    assert obj.value_amount == 89 * 100.5

def test_exams_entity_90_schema_validation():
    obj = ExamsSchemaEntity90Create(
        entity_code="TEST_EXAMS_90",
        name="Test Entity 90",
        value_amount=90 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_90"
    assert obj.value_amount == 90 * 100.5

def test_exams_entity_91_schema_validation():
    obj = ExamsSchemaEntity91Create(
        entity_code="TEST_EXAMS_91",
        name="Test Entity 91",
        value_amount=91 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_91"
    assert obj.value_amount == 91 * 100.5

def test_exams_entity_92_schema_validation():
    obj = ExamsSchemaEntity92Create(
        entity_code="TEST_EXAMS_92",
        name="Test Entity 92",
        value_amount=92 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_92"
    assert obj.value_amount == 92 * 100.5

def test_exams_entity_93_schema_validation():
    obj = ExamsSchemaEntity93Create(
        entity_code="TEST_EXAMS_93",
        name="Test Entity 93",
        value_amount=93 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_93"
    assert obj.value_amount == 93 * 100.5

def test_exams_entity_94_schema_validation():
    obj = ExamsSchemaEntity94Create(
        entity_code="TEST_EXAMS_94",
        name="Test Entity 94",
        value_amount=94 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_94"
    assert obj.value_amount == 94 * 100.5

def test_exams_entity_95_schema_validation():
    obj = ExamsSchemaEntity95Create(
        entity_code="TEST_EXAMS_95",
        name="Test Entity 95",
        value_amount=95 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_95"
    assert obj.value_amount == 95 * 100.5

def test_exams_entity_96_schema_validation():
    obj = ExamsSchemaEntity96Create(
        entity_code="TEST_EXAMS_96",
        name="Test Entity 96",
        value_amount=96 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_96"
    assert obj.value_amount == 96 * 100.5

def test_exams_entity_97_schema_validation():
    obj = ExamsSchemaEntity97Create(
        entity_code="TEST_EXAMS_97",
        name="Test Entity 97",
        value_amount=97 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_97"
    assert obj.value_amount == 97 * 100.5

def test_exams_entity_98_schema_validation():
    obj = ExamsSchemaEntity98Create(
        entity_code="TEST_EXAMS_98",
        name="Test Entity 98",
        value_amount=98 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_98"
    assert obj.value_amount == 98 * 100.5

def test_exams_entity_99_schema_validation():
    obj = ExamsSchemaEntity99Create(
        entity_code="TEST_EXAMS_99",
        name="Test Entity 99",
        value_amount=99 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_99"
    assert obj.value_amount == 99 * 100.5

def test_exams_entity_100_schema_validation():
    obj = ExamsSchemaEntity100Create(
        entity_code="TEST_EXAMS_100",
        name="Test Entity 100",
        value_amount=100 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_100"
    assert obj.value_amount == 100 * 100.5

def test_exams_entity_101_schema_validation():
    obj = ExamsSchemaEntity101Create(
        entity_code="TEST_EXAMS_101",
        name="Test Entity 101",
        value_amount=101 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_101"
    assert obj.value_amount == 101 * 100.5

def test_exams_entity_102_schema_validation():
    obj = ExamsSchemaEntity102Create(
        entity_code="TEST_EXAMS_102",
        name="Test Entity 102",
        value_amount=102 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_102"
    assert obj.value_amount == 102 * 100.5

def test_exams_entity_103_schema_validation():
    obj = ExamsSchemaEntity103Create(
        entity_code="TEST_EXAMS_103",
        name="Test Entity 103",
        value_amount=103 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_103"
    assert obj.value_amount == 103 * 100.5

def test_exams_entity_104_schema_validation():
    obj = ExamsSchemaEntity104Create(
        entity_code="TEST_EXAMS_104",
        name="Test Entity 104",
        value_amount=104 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_104"
    assert obj.value_amount == 104 * 100.5

def test_exams_entity_105_schema_validation():
    obj = ExamsSchemaEntity105Create(
        entity_code="TEST_EXAMS_105",
        name="Test Entity 105",
        value_amount=105 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_105"
    assert obj.value_amount == 105 * 100.5

def test_exams_entity_106_schema_validation():
    obj = ExamsSchemaEntity106Create(
        entity_code="TEST_EXAMS_106",
        name="Test Entity 106",
        value_amount=106 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_106"
    assert obj.value_amount == 106 * 100.5

def test_exams_entity_107_schema_validation():
    obj = ExamsSchemaEntity107Create(
        entity_code="TEST_EXAMS_107",
        name="Test Entity 107",
        value_amount=107 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_107"
    assert obj.value_amount == 107 * 100.5

def test_exams_entity_108_schema_validation():
    obj = ExamsSchemaEntity108Create(
        entity_code="TEST_EXAMS_108",
        name="Test Entity 108",
        value_amount=108 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_108"
    assert obj.value_amount == 108 * 100.5

def test_exams_entity_109_schema_validation():
    obj = ExamsSchemaEntity109Create(
        entity_code="TEST_EXAMS_109",
        name="Test Entity 109",
        value_amount=109 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_109"
    assert obj.value_amount == 109 * 100.5

def test_exams_entity_110_schema_validation():
    obj = ExamsSchemaEntity110Create(
        entity_code="TEST_EXAMS_110",
        name="Test Entity 110",
        value_amount=110 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_110"
    assert obj.value_amount == 110 * 100.5

def test_exams_entity_111_schema_validation():
    obj = ExamsSchemaEntity111Create(
        entity_code="TEST_EXAMS_111",
        name="Test Entity 111",
        value_amount=111 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_111"
    assert obj.value_amount == 111 * 100.5

def test_exams_entity_112_schema_validation():
    obj = ExamsSchemaEntity112Create(
        entity_code="TEST_EXAMS_112",
        name="Test Entity 112",
        value_amount=112 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_112"
    assert obj.value_amount == 112 * 100.5

def test_exams_entity_113_schema_validation():
    obj = ExamsSchemaEntity113Create(
        entity_code="TEST_EXAMS_113",
        name="Test Entity 113",
        value_amount=113 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_113"
    assert obj.value_amount == 113 * 100.5

def test_exams_entity_114_schema_validation():
    obj = ExamsSchemaEntity114Create(
        entity_code="TEST_EXAMS_114",
        name="Test Entity 114",
        value_amount=114 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_114"
    assert obj.value_amount == 114 * 100.5

def test_exams_entity_115_schema_validation():
    obj = ExamsSchemaEntity115Create(
        entity_code="TEST_EXAMS_115",
        name="Test Entity 115",
        value_amount=115 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_115"
    assert obj.value_amount == 115 * 100.5

def test_exams_entity_116_schema_validation():
    obj = ExamsSchemaEntity116Create(
        entity_code="TEST_EXAMS_116",
        name="Test Entity 116",
        value_amount=116 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_116"
    assert obj.value_amount == 116 * 100.5

def test_exams_entity_117_schema_validation():
    obj = ExamsSchemaEntity117Create(
        entity_code="TEST_EXAMS_117",
        name="Test Entity 117",
        value_amount=117 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_117"
    assert obj.value_amount == 117 * 100.5

def test_exams_entity_118_schema_validation():
    obj = ExamsSchemaEntity118Create(
        entity_code="TEST_EXAMS_118",
        name="Test Entity 118",
        value_amount=118 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_118"
    assert obj.value_amount == 118 * 100.5

def test_exams_entity_119_schema_validation():
    obj = ExamsSchemaEntity119Create(
        entity_code="TEST_EXAMS_119",
        name="Test Entity 119",
        value_amount=119 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_119"
    assert obj.value_amount == 119 * 100.5

def test_exams_entity_120_schema_validation():
    obj = ExamsSchemaEntity120Create(
        entity_code="TEST_EXAMS_120",
        name="Test Entity 120",
        value_amount=120 * 100.5
    )
    assert obj.entity_code == "TEST_EXAMS_120"
    assert obj.value_amount == 120 * 100.5


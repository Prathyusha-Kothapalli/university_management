"""
Pytest suite for Library & Digital Repositories
"""
import pytest
from app.domains.library.schemas import *

def test_library_entity_1_schema_validation():
    obj = LibrarySchemaEntity1Create(
        entity_code="TEST_LIBRARY_1",
        name="Test Entity 1",
        value_amount=1 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_1"
    assert obj.value_amount == 1 * 100.5

def test_library_entity_2_schema_validation():
    obj = LibrarySchemaEntity2Create(
        entity_code="TEST_LIBRARY_2",
        name="Test Entity 2",
        value_amount=2 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_2"
    assert obj.value_amount == 2 * 100.5

def test_library_entity_3_schema_validation():
    obj = LibrarySchemaEntity3Create(
        entity_code="TEST_LIBRARY_3",
        name="Test Entity 3",
        value_amount=3 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_3"
    assert obj.value_amount == 3 * 100.5

def test_library_entity_4_schema_validation():
    obj = LibrarySchemaEntity4Create(
        entity_code="TEST_LIBRARY_4",
        name="Test Entity 4",
        value_amount=4 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_4"
    assert obj.value_amount == 4 * 100.5

def test_library_entity_5_schema_validation():
    obj = LibrarySchemaEntity5Create(
        entity_code="TEST_LIBRARY_5",
        name="Test Entity 5",
        value_amount=5 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_5"
    assert obj.value_amount == 5 * 100.5

def test_library_entity_6_schema_validation():
    obj = LibrarySchemaEntity6Create(
        entity_code="TEST_LIBRARY_6",
        name="Test Entity 6",
        value_amount=6 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_6"
    assert obj.value_amount == 6 * 100.5

def test_library_entity_7_schema_validation():
    obj = LibrarySchemaEntity7Create(
        entity_code="TEST_LIBRARY_7",
        name="Test Entity 7",
        value_amount=7 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_7"
    assert obj.value_amount == 7 * 100.5

def test_library_entity_8_schema_validation():
    obj = LibrarySchemaEntity8Create(
        entity_code="TEST_LIBRARY_8",
        name="Test Entity 8",
        value_amount=8 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_8"
    assert obj.value_amount == 8 * 100.5

def test_library_entity_9_schema_validation():
    obj = LibrarySchemaEntity9Create(
        entity_code="TEST_LIBRARY_9",
        name="Test Entity 9",
        value_amount=9 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_9"
    assert obj.value_amount == 9 * 100.5

def test_library_entity_10_schema_validation():
    obj = LibrarySchemaEntity10Create(
        entity_code="TEST_LIBRARY_10",
        name="Test Entity 10",
        value_amount=10 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_10"
    assert obj.value_amount == 10 * 100.5

def test_library_entity_11_schema_validation():
    obj = LibrarySchemaEntity11Create(
        entity_code="TEST_LIBRARY_11",
        name="Test Entity 11",
        value_amount=11 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_11"
    assert obj.value_amount == 11 * 100.5

def test_library_entity_12_schema_validation():
    obj = LibrarySchemaEntity12Create(
        entity_code="TEST_LIBRARY_12",
        name="Test Entity 12",
        value_amount=12 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_12"
    assert obj.value_amount == 12 * 100.5

def test_library_entity_13_schema_validation():
    obj = LibrarySchemaEntity13Create(
        entity_code="TEST_LIBRARY_13",
        name="Test Entity 13",
        value_amount=13 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_13"
    assert obj.value_amount == 13 * 100.5

def test_library_entity_14_schema_validation():
    obj = LibrarySchemaEntity14Create(
        entity_code="TEST_LIBRARY_14",
        name="Test Entity 14",
        value_amount=14 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_14"
    assert obj.value_amount == 14 * 100.5

def test_library_entity_15_schema_validation():
    obj = LibrarySchemaEntity15Create(
        entity_code="TEST_LIBRARY_15",
        name="Test Entity 15",
        value_amount=15 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_15"
    assert obj.value_amount == 15 * 100.5

def test_library_entity_16_schema_validation():
    obj = LibrarySchemaEntity16Create(
        entity_code="TEST_LIBRARY_16",
        name="Test Entity 16",
        value_amount=16 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_16"
    assert obj.value_amount == 16 * 100.5

def test_library_entity_17_schema_validation():
    obj = LibrarySchemaEntity17Create(
        entity_code="TEST_LIBRARY_17",
        name="Test Entity 17",
        value_amount=17 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_17"
    assert obj.value_amount == 17 * 100.5

def test_library_entity_18_schema_validation():
    obj = LibrarySchemaEntity18Create(
        entity_code="TEST_LIBRARY_18",
        name="Test Entity 18",
        value_amount=18 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_18"
    assert obj.value_amount == 18 * 100.5

def test_library_entity_19_schema_validation():
    obj = LibrarySchemaEntity19Create(
        entity_code="TEST_LIBRARY_19",
        name="Test Entity 19",
        value_amount=19 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_19"
    assert obj.value_amount == 19 * 100.5

def test_library_entity_20_schema_validation():
    obj = LibrarySchemaEntity20Create(
        entity_code="TEST_LIBRARY_20",
        name="Test Entity 20",
        value_amount=20 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_20"
    assert obj.value_amount == 20 * 100.5

def test_library_entity_21_schema_validation():
    obj = LibrarySchemaEntity21Create(
        entity_code="TEST_LIBRARY_21",
        name="Test Entity 21",
        value_amount=21 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_21"
    assert obj.value_amount == 21 * 100.5

def test_library_entity_22_schema_validation():
    obj = LibrarySchemaEntity22Create(
        entity_code="TEST_LIBRARY_22",
        name="Test Entity 22",
        value_amount=22 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_22"
    assert obj.value_amount == 22 * 100.5

def test_library_entity_23_schema_validation():
    obj = LibrarySchemaEntity23Create(
        entity_code="TEST_LIBRARY_23",
        name="Test Entity 23",
        value_amount=23 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_23"
    assert obj.value_amount == 23 * 100.5

def test_library_entity_24_schema_validation():
    obj = LibrarySchemaEntity24Create(
        entity_code="TEST_LIBRARY_24",
        name="Test Entity 24",
        value_amount=24 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_24"
    assert obj.value_amount == 24 * 100.5

def test_library_entity_25_schema_validation():
    obj = LibrarySchemaEntity25Create(
        entity_code="TEST_LIBRARY_25",
        name="Test Entity 25",
        value_amount=25 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_25"
    assert obj.value_amount == 25 * 100.5

def test_library_entity_26_schema_validation():
    obj = LibrarySchemaEntity26Create(
        entity_code="TEST_LIBRARY_26",
        name="Test Entity 26",
        value_amount=26 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_26"
    assert obj.value_amount == 26 * 100.5

def test_library_entity_27_schema_validation():
    obj = LibrarySchemaEntity27Create(
        entity_code="TEST_LIBRARY_27",
        name="Test Entity 27",
        value_amount=27 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_27"
    assert obj.value_amount == 27 * 100.5

def test_library_entity_28_schema_validation():
    obj = LibrarySchemaEntity28Create(
        entity_code="TEST_LIBRARY_28",
        name="Test Entity 28",
        value_amount=28 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_28"
    assert obj.value_amount == 28 * 100.5

def test_library_entity_29_schema_validation():
    obj = LibrarySchemaEntity29Create(
        entity_code="TEST_LIBRARY_29",
        name="Test Entity 29",
        value_amount=29 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_29"
    assert obj.value_amount == 29 * 100.5

def test_library_entity_30_schema_validation():
    obj = LibrarySchemaEntity30Create(
        entity_code="TEST_LIBRARY_30",
        name="Test Entity 30",
        value_amount=30 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_30"
    assert obj.value_amount == 30 * 100.5

def test_library_entity_31_schema_validation():
    obj = LibrarySchemaEntity31Create(
        entity_code="TEST_LIBRARY_31",
        name="Test Entity 31",
        value_amount=31 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_31"
    assert obj.value_amount == 31 * 100.5

def test_library_entity_32_schema_validation():
    obj = LibrarySchemaEntity32Create(
        entity_code="TEST_LIBRARY_32",
        name="Test Entity 32",
        value_amount=32 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_32"
    assert obj.value_amount == 32 * 100.5

def test_library_entity_33_schema_validation():
    obj = LibrarySchemaEntity33Create(
        entity_code="TEST_LIBRARY_33",
        name="Test Entity 33",
        value_amount=33 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_33"
    assert obj.value_amount == 33 * 100.5

def test_library_entity_34_schema_validation():
    obj = LibrarySchemaEntity34Create(
        entity_code="TEST_LIBRARY_34",
        name="Test Entity 34",
        value_amount=34 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_34"
    assert obj.value_amount == 34 * 100.5

def test_library_entity_35_schema_validation():
    obj = LibrarySchemaEntity35Create(
        entity_code="TEST_LIBRARY_35",
        name="Test Entity 35",
        value_amount=35 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_35"
    assert obj.value_amount == 35 * 100.5

def test_library_entity_36_schema_validation():
    obj = LibrarySchemaEntity36Create(
        entity_code="TEST_LIBRARY_36",
        name="Test Entity 36",
        value_amount=36 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_36"
    assert obj.value_amount == 36 * 100.5

def test_library_entity_37_schema_validation():
    obj = LibrarySchemaEntity37Create(
        entity_code="TEST_LIBRARY_37",
        name="Test Entity 37",
        value_amount=37 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_37"
    assert obj.value_amount == 37 * 100.5

def test_library_entity_38_schema_validation():
    obj = LibrarySchemaEntity38Create(
        entity_code="TEST_LIBRARY_38",
        name="Test Entity 38",
        value_amount=38 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_38"
    assert obj.value_amount == 38 * 100.5

def test_library_entity_39_schema_validation():
    obj = LibrarySchemaEntity39Create(
        entity_code="TEST_LIBRARY_39",
        name="Test Entity 39",
        value_amount=39 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_39"
    assert obj.value_amount == 39 * 100.5

def test_library_entity_40_schema_validation():
    obj = LibrarySchemaEntity40Create(
        entity_code="TEST_LIBRARY_40",
        name="Test Entity 40",
        value_amount=40 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_40"
    assert obj.value_amount == 40 * 100.5

def test_library_entity_41_schema_validation():
    obj = LibrarySchemaEntity41Create(
        entity_code="TEST_LIBRARY_41",
        name="Test Entity 41",
        value_amount=41 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_41"
    assert obj.value_amount == 41 * 100.5

def test_library_entity_42_schema_validation():
    obj = LibrarySchemaEntity42Create(
        entity_code="TEST_LIBRARY_42",
        name="Test Entity 42",
        value_amount=42 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_42"
    assert obj.value_amount == 42 * 100.5

def test_library_entity_43_schema_validation():
    obj = LibrarySchemaEntity43Create(
        entity_code="TEST_LIBRARY_43",
        name="Test Entity 43",
        value_amount=43 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_43"
    assert obj.value_amount == 43 * 100.5

def test_library_entity_44_schema_validation():
    obj = LibrarySchemaEntity44Create(
        entity_code="TEST_LIBRARY_44",
        name="Test Entity 44",
        value_amount=44 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_44"
    assert obj.value_amount == 44 * 100.5

def test_library_entity_45_schema_validation():
    obj = LibrarySchemaEntity45Create(
        entity_code="TEST_LIBRARY_45",
        name="Test Entity 45",
        value_amount=45 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_45"
    assert obj.value_amount == 45 * 100.5

def test_library_entity_46_schema_validation():
    obj = LibrarySchemaEntity46Create(
        entity_code="TEST_LIBRARY_46",
        name="Test Entity 46",
        value_amount=46 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_46"
    assert obj.value_amount == 46 * 100.5

def test_library_entity_47_schema_validation():
    obj = LibrarySchemaEntity47Create(
        entity_code="TEST_LIBRARY_47",
        name="Test Entity 47",
        value_amount=47 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_47"
    assert obj.value_amount == 47 * 100.5

def test_library_entity_48_schema_validation():
    obj = LibrarySchemaEntity48Create(
        entity_code="TEST_LIBRARY_48",
        name="Test Entity 48",
        value_amount=48 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_48"
    assert obj.value_amount == 48 * 100.5

def test_library_entity_49_schema_validation():
    obj = LibrarySchemaEntity49Create(
        entity_code="TEST_LIBRARY_49",
        name="Test Entity 49",
        value_amount=49 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_49"
    assert obj.value_amount == 49 * 100.5

def test_library_entity_50_schema_validation():
    obj = LibrarySchemaEntity50Create(
        entity_code="TEST_LIBRARY_50",
        name="Test Entity 50",
        value_amount=50 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_50"
    assert obj.value_amount == 50 * 100.5

def test_library_entity_51_schema_validation():
    obj = LibrarySchemaEntity51Create(
        entity_code="TEST_LIBRARY_51",
        name="Test Entity 51",
        value_amount=51 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_51"
    assert obj.value_amount == 51 * 100.5

def test_library_entity_52_schema_validation():
    obj = LibrarySchemaEntity52Create(
        entity_code="TEST_LIBRARY_52",
        name="Test Entity 52",
        value_amount=52 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_52"
    assert obj.value_amount == 52 * 100.5

def test_library_entity_53_schema_validation():
    obj = LibrarySchemaEntity53Create(
        entity_code="TEST_LIBRARY_53",
        name="Test Entity 53",
        value_amount=53 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_53"
    assert obj.value_amount == 53 * 100.5

def test_library_entity_54_schema_validation():
    obj = LibrarySchemaEntity54Create(
        entity_code="TEST_LIBRARY_54",
        name="Test Entity 54",
        value_amount=54 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_54"
    assert obj.value_amount == 54 * 100.5

def test_library_entity_55_schema_validation():
    obj = LibrarySchemaEntity55Create(
        entity_code="TEST_LIBRARY_55",
        name="Test Entity 55",
        value_amount=55 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_55"
    assert obj.value_amount == 55 * 100.5

def test_library_entity_56_schema_validation():
    obj = LibrarySchemaEntity56Create(
        entity_code="TEST_LIBRARY_56",
        name="Test Entity 56",
        value_amount=56 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_56"
    assert obj.value_amount == 56 * 100.5

def test_library_entity_57_schema_validation():
    obj = LibrarySchemaEntity57Create(
        entity_code="TEST_LIBRARY_57",
        name="Test Entity 57",
        value_amount=57 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_57"
    assert obj.value_amount == 57 * 100.5

def test_library_entity_58_schema_validation():
    obj = LibrarySchemaEntity58Create(
        entity_code="TEST_LIBRARY_58",
        name="Test Entity 58",
        value_amount=58 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_58"
    assert obj.value_amount == 58 * 100.5

def test_library_entity_59_schema_validation():
    obj = LibrarySchemaEntity59Create(
        entity_code="TEST_LIBRARY_59",
        name="Test Entity 59",
        value_amount=59 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_59"
    assert obj.value_amount == 59 * 100.5

def test_library_entity_60_schema_validation():
    obj = LibrarySchemaEntity60Create(
        entity_code="TEST_LIBRARY_60",
        name="Test Entity 60",
        value_amount=60 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_60"
    assert obj.value_amount == 60 * 100.5

def test_library_entity_61_schema_validation():
    obj = LibrarySchemaEntity61Create(
        entity_code="TEST_LIBRARY_61",
        name="Test Entity 61",
        value_amount=61 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_61"
    assert obj.value_amount == 61 * 100.5

def test_library_entity_62_schema_validation():
    obj = LibrarySchemaEntity62Create(
        entity_code="TEST_LIBRARY_62",
        name="Test Entity 62",
        value_amount=62 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_62"
    assert obj.value_amount == 62 * 100.5

def test_library_entity_63_schema_validation():
    obj = LibrarySchemaEntity63Create(
        entity_code="TEST_LIBRARY_63",
        name="Test Entity 63",
        value_amount=63 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_63"
    assert obj.value_amount == 63 * 100.5

def test_library_entity_64_schema_validation():
    obj = LibrarySchemaEntity64Create(
        entity_code="TEST_LIBRARY_64",
        name="Test Entity 64",
        value_amount=64 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_64"
    assert obj.value_amount == 64 * 100.5

def test_library_entity_65_schema_validation():
    obj = LibrarySchemaEntity65Create(
        entity_code="TEST_LIBRARY_65",
        name="Test Entity 65",
        value_amount=65 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_65"
    assert obj.value_amount == 65 * 100.5

def test_library_entity_66_schema_validation():
    obj = LibrarySchemaEntity66Create(
        entity_code="TEST_LIBRARY_66",
        name="Test Entity 66",
        value_amount=66 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_66"
    assert obj.value_amount == 66 * 100.5

def test_library_entity_67_schema_validation():
    obj = LibrarySchemaEntity67Create(
        entity_code="TEST_LIBRARY_67",
        name="Test Entity 67",
        value_amount=67 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_67"
    assert obj.value_amount == 67 * 100.5

def test_library_entity_68_schema_validation():
    obj = LibrarySchemaEntity68Create(
        entity_code="TEST_LIBRARY_68",
        name="Test Entity 68",
        value_amount=68 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_68"
    assert obj.value_amount == 68 * 100.5

def test_library_entity_69_schema_validation():
    obj = LibrarySchemaEntity69Create(
        entity_code="TEST_LIBRARY_69",
        name="Test Entity 69",
        value_amount=69 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_69"
    assert obj.value_amount == 69 * 100.5

def test_library_entity_70_schema_validation():
    obj = LibrarySchemaEntity70Create(
        entity_code="TEST_LIBRARY_70",
        name="Test Entity 70",
        value_amount=70 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_70"
    assert obj.value_amount == 70 * 100.5

def test_library_entity_71_schema_validation():
    obj = LibrarySchemaEntity71Create(
        entity_code="TEST_LIBRARY_71",
        name="Test Entity 71",
        value_amount=71 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_71"
    assert obj.value_amount == 71 * 100.5

def test_library_entity_72_schema_validation():
    obj = LibrarySchemaEntity72Create(
        entity_code="TEST_LIBRARY_72",
        name="Test Entity 72",
        value_amount=72 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_72"
    assert obj.value_amount == 72 * 100.5

def test_library_entity_73_schema_validation():
    obj = LibrarySchemaEntity73Create(
        entity_code="TEST_LIBRARY_73",
        name="Test Entity 73",
        value_amount=73 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_73"
    assert obj.value_amount == 73 * 100.5

def test_library_entity_74_schema_validation():
    obj = LibrarySchemaEntity74Create(
        entity_code="TEST_LIBRARY_74",
        name="Test Entity 74",
        value_amount=74 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_74"
    assert obj.value_amount == 74 * 100.5

def test_library_entity_75_schema_validation():
    obj = LibrarySchemaEntity75Create(
        entity_code="TEST_LIBRARY_75",
        name="Test Entity 75",
        value_amount=75 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_75"
    assert obj.value_amount == 75 * 100.5

def test_library_entity_76_schema_validation():
    obj = LibrarySchemaEntity76Create(
        entity_code="TEST_LIBRARY_76",
        name="Test Entity 76",
        value_amount=76 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_76"
    assert obj.value_amount == 76 * 100.5

def test_library_entity_77_schema_validation():
    obj = LibrarySchemaEntity77Create(
        entity_code="TEST_LIBRARY_77",
        name="Test Entity 77",
        value_amount=77 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_77"
    assert obj.value_amount == 77 * 100.5

def test_library_entity_78_schema_validation():
    obj = LibrarySchemaEntity78Create(
        entity_code="TEST_LIBRARY_78",
        name="Test Entity 78",
        value_amount=78 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_78"
    assert obj.value_amount == 78 * 100.5

def test_library_entity_79_schema_validation():
    obj = LibrarySchemaEntity79Create(
        entity_code="TEST_LIBRARY_79",
        name="Test Entity 79",
        value_amount=79 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_79"
    assert obj.value_amount == 79 * 100.5

def test_library_entity_80_schema_validation():
    obj = LibrarySchemaEntity80Create(
        entity_code="TEST_LIBRARY_80",
        name="Test Entity 80",
        value_amount=80 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_80"
    assert obj.value_amount == 80 * 100.5

def test_library_entity_81_schema_validation():
    obj = LibrarySchemaEntity81Create(
        entity_code="TEST_LIBRARY_81",
        name="Test Entity 81",
        value_amount=81 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_81"
    assert obj.value_amount == 81 * 100.5

def test_library_entity_82_schema_validation():
    obj = LibrarySchemaEntity82Create(
        entity_code="TEST_LIBRARY_82",
        name="Test Entity 82",
        value_amount=82 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_82"
    assert obj.value_amount == 82 * 100.5

def test_library_entity_83_schema_validation():
    obj = LibrarySchemaEntity83Create(
        entity_code="TEST_LIBRARY_83",
        name="Test Entity 83",
        value_amount=83 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_83"
    assert obj.value_amount == 83 * 100.5

def test_library_entity_84_schema_validation():
    obj = LibrarySchemaEntity84Create(
        entity_code="TEST_LIBRARY_84",
        name="Test Entity 84",
        value_amount=84 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_84"
    assert obj.value_amount == 84 * 100.5

def test_library_entity_85_schema_validation():
    obj = LibrarySchemaEntity85Create(
        entity_code="TEST_LIBRARY_85",
        name="Test Entity 85",
        value_amount=85 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_85"
    assert obj.value_amount == 85 * 100.5

def test_library_entity_86_schema_validation():
    obj = LibrarySchemaEntity86Create(
        entity_code="TEST_LIBRARY_86",
        name="Test Entity 86",
        value_amount=86 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_86"
    assert obj.value_amount == 86 * 100.5

def test_library_entity_87_schema_validation():
    obj = LibrarySchemaEntity87Create(
        entity_code="TEST_LIBRARY_87",
        name="Test Entity 87",
        value_amount=87 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_87"
    assert obj.value_amount == 87 * 100.5

def test_library_entity_88_schema_validation():
    obj = LibrarySchemaEntity88Create(
        entity_code="TEST_LIBRARY_88",
        name="Test Entity 88",
        value_amount=88 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_88"
    assert obj.value_amount == 88 * 100.5

def test_library_entity_89_schema_validation():
    obj = LibrarySchemaEntity89Create(
        entity_code="TEST_LIBRARY_89",
        name="Test Entity 89",
        value_amount=89 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_89"
    assert obj.value_amount == 89 * 100.5

def test_library_entity_90_schema_validation():
    obj = LibrarySchemaEntity90Create(
        entity_code="TEST_LIBRARY_90",
        name="Test Entity 90",
        value_amount=90 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_90"
    assert obj.value_amount == 90 * 100.5

def test_library_entity_91_schema_validation():
    obj = LibrarySchemaEntity91Create(
        entity_code="TEST_LIBRARY_91",
        name="Test Entity 91",
        value_amount=91 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_91"
    assert obj.value_amount == 91 * 100.5

def test_library_entity_92_schema_validation():
    obj = LibrarySchemaEntity92Create(
        entity_code="TEST_LIBRARY_92",
        name="Test Entity 92",
        value_amount=92 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_92"
    assert obj.value_amount == 92 * 100.5

def test_library_entity_93_schema_validation():
    obj = LibrarySchemaEntity93Create(
        entity_code="TEST_LIBRARY_93",
        name="Test Entity 93",
        value_amount=93 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_93"
    assert obj.value_amount == 93 * 100.5

def test_library_entity_94_schema_validation():
    obj = LibrarySchemaEntity94Create(
        entity_code="TEST_LIBRARY_94",
        name="Test Entity 94",
        value_amount=94 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_94"
    assert obj.value_amount == 94 * 100.5

def test_library_entity_95_schema_validation():
    obj = LibrarySchemaEntity95Create(
        entity_code="TEST_LIBRARY_95",
        name="Test Entity 95",
        value_amount=95 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_95"
    assert obj.value_amount == 95 * 100.5

def test_library_entity_96_schema_validation():
    obj = LibrarySchemaEntity96Create(
        entity_code="TEST_LIBRARY_96",
        name="Test Entity 96",
        value_amount=96 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_96"
    assert obj.value_amount == 96 * 100.5

def test_library_entity_97_schema_validation():
    obj = LibrarySchemaEntity97Create(
        entity_code="TEST_LIBRARY_97",
        name="Test Entity 97",
        value_amount=97 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_97"
    assert obj.value_amount == 97 * 100.5

def test_library_entity_98_schema_validation():
    obj = LibrarySchemaEntity98Create(
        entity_code="TEST_LIBRARY_98",
        name="Test Entity 98",
        value_amount=98 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_98"
    assert obj.value_amount == 98 * 100.5

def test_library_entity_99_schema_validation():
    obj = LibrarySchemaEntity99Create(
        entity_code="TEST_LIBRARY_99",
        name="Test Entity 99",
        value_amount=99 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_99"
    assert obj.value_amount == 99 * 100.5

def test_library_entity_100_schema_validation():
    obj = LibrarySchemaEntity100Create(
        entity_code="TEST_LIBRARY_100",
        name="Test Entity 100",
        value_amount=100 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_100"
    assert obj.value_amount == 100 * 100.5

def test_library_entity_101_schema_validation():
    obj = LibrarySchemaEntity101Create(
        entity_code="TEST_LIBRARY_101",
        name="Test Entity 101",
        value_amount=101 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_101"
    assert obj.value_amount == 101 * 100.5

def test_library_entity_102_schema_validation():
    obj = LibrarySchemaEntity102Create(
        entity_code="TEST_LIBRARY_102",
        name="Test Entity 102",
        value_amount=102 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_102"
    assert obj.value_amount == 102 * 100.5

def test_library_entity_103_schema_validation():
    obj = LibrarySchemaEntity103Create(
        entity_code="TEST_LIBRARY_103",
        name="Test Entity 103",
        value_amount=103 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_103"
    assert obj.value_amount == 103 * 100.5

def test_library_entity_104_schema_validation():
    obj = LibrarySchemaEntity104Create(
        entity_code="TEST_LIBRARY_104",
        name="Test Entity 104",
        value_amount=104 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_104"
    assert obj.value_amount == 104 * 100.5

def test_library_entity_105_schema_validation():
    obj = LibrarySchemaEntity105Create(
        entity_code="TEST_LIBRARY_105",
        name="Test Entity 105",
        value_amount=105 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_105"
    assert obj.value_amount == 105 * 100.5

def test_library_entity_106_schema_validation():
    obj = LibrarySchemaEntity106Create(
        entity_code="TEST_LIBRARY_106",
        name="Test Entity 106",
        value_amount=106 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_106"
    assert obj.value_amount == 106 * 100.5

def test_library_entity_107_schema_validation():
    obj = LibrarySchemaEntity107Create(
        entity_code="TEST_LIBRARY_107",
        name="Test Entity 107",
        value_amount=107 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_107"
    assert obj.value_amount == 107 * 100.5

def test_library_entity_108_schema_validation():
    obj = LibrarySchemaEntity108Create(
        entity_code="TEST_LIBRARY_108",
        name="Test Entity 108",
        value_amount=108 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_108"
    assert obj.value_amount == 108 * 100.5

def test_library_entity_109_schema_validation():
    obj = LibrarySchemaEntity109Create(
        entity_code="TEST_LIBRARY_109",
        name="Test Entity 109",
        value_amount=109 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_109"
    assert obj.value_amount == 109 * 100.5

def test_library_entity_110_schema_validation():
    obj = LibrarySchemaEntity110Create(
        entity_code="TEST_LIBRARY_110",
        name="Test Entity 110",
        value_amount=110 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_110"
    assert obj.value_amount == 110 * 100.5

def test_library_entity_111_schema_validation():
    obj = LibrarySchemaEntity111Create(
        entity_code="TEST_LIBRARY_111",
        name="Test Entity 111",
        value_amount=111 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_111"
    assert obj.value_amount == 111 * 100.5

def test_library_entity_112_schema_validation():
    obj = LibrarySchemaEntity112Create(
        entity_code="TEST_LIBRARY_112",
        name="Test Entity 112",
        value_amount=112 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_112"
    assert obj.value_amount == 112 * 100.5

def test_library_entity_113_schema_validation():
    obj = LibrarySchemaEntity113Create(
        entity_code="TEST_LIBRARY_113",
        name="Test Entity 113",
        value_amount=113 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_113"
    assert obj.value_amount == 113 * 100.5

def test_library_entity_114_schema_validation():
    obj = LibrarySchemaEntity114Create(
        entity_code="TEST_LIBRARY_114",
        name="Test Entity 114",
        value_amount=114 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_114"
    assert obj.value_amount == 114 * 100.5

def test_library_entity_115_schema_validation():
    obj = LibrarySchemaEntity115Create(
        entity_code="TEST_LIBRARY_115",
        name="Test Entity 115",
        value_amount=115 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_115"
    assert obj.value_amount == 115 * 100.5

def test_library_entity_116_schema_validation():
    obj = LibrarySchemaEntity116Create(
        entity_code="TEST_LIBRARY_116",
        name="Test Entity 116",
        value_amount=116 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_116"
    assert obj.value_amount == 116 * 100.5

def test_library_entity_117_schema_validation():
    obj = LibrarySchemaEntity117Create(
        entity_code="TEST_LIBRARY_117",
        name="Test Entity 117",
        value_amount=117 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_117"
    assert obj.value_amount == 117 * 100.5

def test_library_entity_118_schema_validation():
    obj = LibrarySchemaEntity118Create(
        entity_code="TEST_LIBRARY_118",
        name="Test Entity 118",
        value_amount=118 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_118"
    assert obj.value_amount == 118 * 100.5

def test_library_entity_119_schema_validation():
    obj = LibrarySchemaEntity119Create(
        entity_code="TEST_LIBRARY_119",
        name="Test Entity 119",
        value_amount=119 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_119"
    assert obj.value_amount == 119 * 100.5

def test_library_entity_120_schema_validation():
    obj = LibrarySchemaEntity120Create(
        entity_code="TEST_LIBRARY_120",
        name="Test Entity 120",
        value_amount=120 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_120"
    assert obj.value_amount == 120 * 100.5

def test_library_entity_121_schema_validation():
    obj = LibrarySchemaEntity121Create(
        entity_code="TEST_LIBRARY_121",
        name="Test Entity 121",
        value_amount=121 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_121"
    assert obj.value_amount == 121 * 100.5

def test_library_entity_122_schema_validation():
    obj = LibrarySchemaEntity122Create(
        entity_code="TEST_LIBRARY_122",
        name="Test Entity 122",
        value_amount=122 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_122"
    assert obj.value_amount == 122 * 100.5

def test_library_entity_123_schema_validation():
    obj = LibrarySchemaEntity123Create(
        entity_code="TEST_LIBRARY_123",
        name="Test Entity 123",
        value_amount=123 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_123"
    assert obj.value_amount == 123 * 100.5

def test_library_entity_124_schema_validation():
    obj = LibrarySchemaEntity124Create(
        entity_code="TEST_LIBRARY_124",
        name="Test Entity 124",
        value_amount=124 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_124"
    assert obj.value_amount == 124 * 100.5

def test_library_entity_125_schema_validation():
    obj = LibrarySchemaEntity125Create(
        entity_code="TEST_LIBRARY_125",
        name="Test Entity 125",
        value_amount=125 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_125"
    assert obj.value_amount == 125 * 100.5

def test_library_entity_126_schema_validation():
    obj = LibrarySchemaEntity126Create(
        entity_code="TEST_LIBRARY_126",
        name="Test Entity 126",
        value_amount=126 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_126"
    assert obj.value_amount == 126 * 100.5

def test_library_entity_127_schema_validation():
    obj = LibrarySchemaEntity127Create(
        entity_code="TEST_LIBRARY_127",
        name="Test Entity 127",
        value_amount=127 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_127"
    assert obj.value_amount == 127 * 100.5

def test_library_entity_128_schema_validation():
    obj = LibrarySchemaEntity128Create(
        entity_code="TEST_LIBRARY_128",
        name="Test Entity 128",
        value_amount=128 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_128"
    assert obj.value_amount == 128 * 100.5

def test_library_entity_129_schema_validation():
    obj = LibrarySchemaEntity129Create(
        entity_code="TEST_LIBRARY_129",
        name="Test Entity 129",
        value_amount=129 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_129"
    assert obj.value_amount == 129 * 100.5

def test_library_entity_130_schema_validation():
    obj = LibrarySchemaEntity130Create(
        entity_code="TEST_LIBRARY_130",
        name="Test Entity 130",
        value_amount=130 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_130"
    assert obj.value_amount == 130 * 100.5

def test_library_entity_131_schema_validation():
    obj = LibrarySchemaEntity131Create(
        entity_code="TEST_LIBRARY_131",
        name="Test Entity 131",
        value_amount=131 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_131"
    assert obj.value_amount == 131 * 100.5

def test_library_entity_132_schema_validation():
    obj = LibrarySchemaEntity132Create(
        entity_code="TEST_LIBRARY_132",
        name="Test Entity 132",
        value_amount=132 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_132"
    assert obj.value_amount == 132 * 100.5

def test_library_entity_133_schema_validation():
    obj = LibrarySchemaEntity133Create(
        entity_code="TEST_LIBRARY_133",
        name="Test Entity 133",
        value_amount=133 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_133"
    assert obj.value_amount == 133 * 100.5

def test_library_entity_134_schema_validation():
    obj = LibrarySchemaEntity134Create(
        entity_code="TEST_LIBRARY_134",
        name="Test Entity 134",
        value_amount=134 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_134"
    assert obj.value_amount == 134 * 100.5

def test_library_entity_135_schema_validation():
    obj = LibrarySchemaEntity135Create(
        entity_code="TEST_LIBRARY_135",
        name="Test Entity 135",
        value_amount=135 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_135"
    assert obj.value_amount == 135 * 100.5

def test_library_entity_136_schema_validation():
    obj = LibrarySchemaEntity136Create(
        entity_code="TEST_LIBRARY_136",
        name="Test Entity 136",
        value_amount=136 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_136"
    assert obj.value_amount == 136 * 100.5

def test_library_entity_137_schema_validation():
    obj = LibrarySchemaEntity137Create(
        entity_code="TEST_LIBRARY_137",
        name="Test Entity 137",
        value_amount=137 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_137"
    assert obj.value_amount == 137 * 100.5

def test_library_entity_138_schema_validation():
    obj = LibrarySchemaEntity138Create(
        entity_code="TEST_LIBRARY_138",
        name="Test Entity 138",
        value_amount=138 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_138"
    assert obj.value_amount == 138 * 100.5

def test_library_entity_139_schema_validation():
    obj = LibrarySchemaEntity139Create(
        entity_code="TEST_LIBRARY_139",
        name="Test Entity 139",
        value_amount=139 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_139"
    assert obj.value_amount == 139 * 100.5

def test_library_entity_140_schema_validation():
    obj = LibrarySchemaEntity140Create(
        entity_code="TEST_LIBRARY_140",
        name="Test Entity 140",
        value_amount=140 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_140"
    assert obj.value_amount == 140 * 100.5

def test_library_entity_141_schema_validation():
    obj = LibrarySchemaEntity141Create(
        entity_code="TEST_LIBRARY_141",
        name="Test Entity 141",
        value_amount=141 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_141"
    assert obj.value_amount == 141 * 100.5

def test_library_entity_142_schema_validation():
    obj = LibrarySchemaEntity142Create(
        entity_code="TEST_LIBRARY_142",
        name="Test Entity 142",
        value_amount=142 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_142"
    assert obj.value_amount == 142 * 100.5

def test_library_entity_143_schema_validation():
    obj = LibrarySchemaEntity143Create(
        entity_code="TEST_LIBRARY_143",
        name="Test Entity 143",
        value_amount=143 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_143"
    assert obj.value_amount == 143 * 100.5

def test_library_entity_144_schema_validation():
    obj = LibrarySchemaEntity144Create(
        entity_code="TEST_LIBRARY_144",
        name="Test Entity 144",
        value_amount=144 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_144"
    assert obj.value_amount == 144 * 100.5

def test_library_entity_145_schema_validation():
    obj = LibrarySchemaEntity145Create(
        entity_code="TEST_LIBRARY_145",
        name="Test Entity 145",
        value_amount=145 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_145"
    assert obj.value_amount == 145 * 100.5

def test_library_entity_146_schema_validation():
    obj = LibrarySchemaEntity146Create(
        entity_code="TEST_LIBRARY_146",
        name="Test Entity 146",
        value_amount=146 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_146"
    assert obj.value_amount == 146 * 100.5

def test_library_entity_147_schema_validation():
    obj = LibrarySchemaEntity147Create(
        entity_code="TEST_LIBRARY_147",
        name="Test Entity 147",
        value_amount=147 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_147"
    assert obj.value_amount == 147 * 100.5

def test_library_entity_148_schema_validation():
    obj = LibrarySchemaEntity148Create(
        entity_code="TEST_LIBRARY_148",
        name="Test Entity 148",
        value_amount=148 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_148"
    assert obj.value_amount == 148 * 100.5

def test_library_entity_149_schema_validation():
    obj = LibrarySchemaEntity149Create(
        entity_code="TEST_LIBRARY_149",
        name="Test Entity 149",
        value_amount=149 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_149"
    assert obj.value_amount == 149 * 100.5

def test_library_entity_150_schema_validation():
    obj = LibrarySchemaEntity150Create(
        entity_code="TEST_LIBRARY_150",
        name="Test Entity 150",
        value_amount=150 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_150"
    assert obj.value_amount == 150 * 100.5

def test_library_entity_151_schema_validation():
    obj = LibrarySchemaEntity151Create(
        entity_code="TEST_LIBRARY_151",
        name="Test Entity 151",
        value_amount=151 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_151"
    assert obj.value_amount == 151 * 100.5

def test_library_entity_152_schema_validation():
    obj = LibrarySchemaEntity152Create(
        entity_code="TEST_LIBRARY_152",
        name="Test Entity 152",
        value_amount=152 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_152"
    assert obj.value_amount == 152 * 100.5

def test_library_entity_153_schema_validation():
    obj = LibrarySchemaEntity153Create(
        entity_code="TEST_LIBRARY_153",
        name="Test Entity 153",
        value_amount=153 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_153"
    assert obj.value_amount == 153 * 100.5

def test_library_entity_154_schema_validation():
    obj = LibrarySchemaEntity154Create(
        entity_code="TEST_LIBRARY_154",
        name="Test Entity 154",
        value_amount=154 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_154"
    assert obj.value_amount == 154 * 100.5

def test_library_entity_155_schema_validation():
    obj = LibrarySchemaEntity155Create(
        entity_code="TEST_LIBRARY_155",
        name="Test Entity 155",
        value_amount=155 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_155"
    assert obj.value_amount == 155 * 100.5

def test_library_entity_156_schema_validation():
    obj = LibrarySchemaEntity156Create(
        entity_code="TEST_LIBRARY_156",
        name="Test Entity 156",
        value_amount=156 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_156"
    assert obj.value_amount == 156 * 100.5

def test_library_entity_157_schema_validation():
    obj = LibrarySchemaEntity157Create(
        entity_code="TEST_LIBRARY_157",
        name="Test Entity 157",
        value_amount=157 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_157"
    assert obj.value_amount == 157 * 100.5

def test_library_entity_158_schema_validation():
    obj = LibrarySchemaEntity158Create(
        entity_code="TEST_LIBRARY_158",
        name="Test Entity 158",
        value_amount=158 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_158"
    assert obj.value_amount == 158 * 100.5

def test_library_entity_159_schema_validation():
    obj = LibrarySchemaEntity159Create(
        entity_code="TEST_LIBRARY_159",
        name="Test Entity 159",
        value_amount=159 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_159"
    assert obj.value_amount == 159 * 100.5

def test_library_entity_160_schema_validation():
    obj = LibrarySchemaEntity160Create(
        entity_code="TEST_LIBRARY_160",
        name="Test Entity 160",
        value_amount=160 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_160"
    assert obj.value_amount == 160 * 100.5

def test_library_entity_161_schema_validation():
    obj = LibrarySchemaEntity161Create(
        entity_code="TEST_LIBRARY_161",
        name="Test Entity 161",
        value_amount=161 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_161"
    assert obj.value_amount == 161 * 100.5

def test_library_entity_162_schema_validation():
    obj = LibrarySchemaEntity162Create(
        entity_code="TEST_LIBRARY_162",
        name="Test Entity 162",
        value_amount=162 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_162"
    assert obj.value_amount == 162 * 100.5

def test_library_entity_163_schema_validation():
    obj = LibrarySchemaEntity163Create(
        entity_code="TEST_LIBRARY_163",
        name="Test Entity 163",
        value_amount=163 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_163"
    assert obj.value_amount == 163 * 100.5

def test_library_entity_164_schema_validation():
    obj = LibrarySchemaEntity164Create(
        entity_code="TEST_LIBRARY_164",
        name="Test Entity 164",
        value_amount=164 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_164"
    assert obj.value_amount == 164 * 100.5

def test_library_entity_165_schema_validation():
    obj = LibrarySchemaEntity165Create(
        entity_code="TEST_LIBRARY_165",
        name="Test Entity 165",
        value_amount=165 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_165"
    assert obj.value_amount == 165 * 100.5

def test_library_entity_166_schema_validation():
    obj = LibrarySchemaEntity166Create(
        entity_code="TEST_LIBRARY_166",
        name="Test Entity 166",
        value_amount=166 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_166"
    assert obj.value_amount == 166 * 100.5

def test_library_entity_167_schema_validation():
    obj = LibrarySchemaEntity167Create(
        entity_code="TEST_LIBRARY_167",
        name="Test Entity 167",
        value_amount=167 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_167"
    assert obj.value_amount == 167 * 100.5

def test_library_entity_168_schema_validation():
    obj = LibrarySchemaEntity168Create(
        entity_code="TEST_LIBRARY_168",
        name="Test Entity 168",
        value_amount=168 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_168"
    assert obj.value_amount == 168 * 100.5

def test_library_entity_169_schema_validation():
    obj = LibrarySchemaEntity169Create(
        entity_code="TEST_LIBRARY_169",
        name="Test Entity 169",
        value_amount=169 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_169"
    assert obj.value_amount == 169 * 100.5

def test_library_entity_170_schema_validation():
    obj = LibrarySchemaEntity170Create(
        entity_code="TEST_LIBRARY_170",
        name="Test Entity 170",
        value_amount=170 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_170"
    assert obj.value_amount == 170 * 100.5

def test_library_entity_171_schema_validation():
    obj = LibrarySchemaEntity171Create(
        entity_code="TEST_LIBRARY_171",
        name="Test Entity 171",
        value_amount=171 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_171"
    assert obj.value_amount == 171 * 100.5

def test_library_entity_172_schema_validation():
    obj = LibrarySchemaEntity172Create(
        entity_code="TEST_LIBRARY_172",
        name="Test Entity 172",
        value_amount=172 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_172"
    assert obj.value_amount == 172 * 100.5

def test_library_entity_173_schema_validation():
    obj = LibrarySchemaEntity173Create(
        entity_code="TEST_LIBRARY_173",
        name="Test Entity 173",
        value_amount=173 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_173"
    assert obj.value_amount == 173 * 100.5

def test_library_entity_174_schema_validation():
    obj = LibrarySchemaEntity174Create(
        entity_code="TEST_LIBRARY_174",
        name="Test Entity 174",
        value_amount=174 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_174"
    assert obj.value_amount == 174 * 100.5

def test_library_entity_175_schema_validation():
    obj = LibrarySchemaEntity175Create(
        entity_code="TEST_LIBRARY_175",
        name="Test Entity 175",
        value_amount=175 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_175"
    assert obj.value_amount == 175 * 100.5

def test_library_entity_176_schema_validation():
    obj = LibrarySchemaEntity176Create(
        entity_code="TEST_LIBRARY_176",
        name="Test Entity 176",
        value_amount=176 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_176"
    assert obj.value_amount == 176 * 100.5

def test_library_entity_177_schema_validation():
    obj = LibrarySchemaEntity177Create(
        entity_code="TEST_LIBRARY_177",
        name="Test Entity 177",
        value_amount=177 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_177"
    assert obj.value_amount == 177 * 100.5

def test_library_entity_178_schema_validation():
    obj = LibrarySchemaEntity178Create(
        entity_code="TEST_LIBRARY_178",
        name="Test Entity 178",
        value_amount=178 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_178"
    assert obj.value_amount == 178 * 100.5

def test_library_entity_179_schema_validation():
    obj = LibrarySchemaEntity179Create(
        entity_code="TEST_LIBRARY_179",
        name="Test Entity 179",
        value_amount=179 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_179"
    assert obj.value_amount == 179 * 100.5

def test_library_entity_180_schema_validation():
    obj = LibrarySchemaEntity180Create(
        entity_code="TEST_LIBRARY_180",
        name="Test Entity 180",
        value_amount=180 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_180"
    assert obj.value_amount == 180 * 100.5

def test_library_entity_181_schema_validation():
    obj = LibrarySchemaEntity181Create(
        entity_code="TEST_LIBRARY_181",
        name="Test Entity 181",
        value_amount=181 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_181"
    assert obj.value_amount == 181 * 100.5

def test_library_entity_182_schema_validation():
    obj = LibrarySchemaEntity182Create(
        entity_code="TEST_LIBRARY_182",
        name="Test Entity 182",
        value_amount=182 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_182"
    assert obj.value_amount == 182 * 100.5

def test_library_entity_183_schema_validation():
    obj = LibrarySchemaEntity183Create(
        entity_code="TEST_LIBRARY_183",
        name="Test Entity 183",
        value_amount=183 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_183"
    assert obj.value_amount == 183 * 100.5

def test_library_entity_184_schema_validation():
    obj = LibrarySchemaEntity184Create(
        entity_code="TEST_LIBRARY_184",
        name="Test Entity 184",
        value_amount=184 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_184"
    assert obj.value_amount == 184 * 100.5

def test_library_entity_185_schema_validation():
    obj = LibrarySchemaEntity185Create(
        entity_code="TEST_LIBRARY_185",
        name="Test Entity 185",
        value_amount=185 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_185"
    assert obj.value_amount == 185 * 100.5

def test_library_entity_186_schema_validation():
    obj = LibrarySchemaEntity186Create(
        entity_code="TEST_LIBRARY_186",
        name="Test Entity 186",
        value_amount=186 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_186"
    assert obj.value_amount == 186 * 100.5

def test_library_entity_187_schema_validation():
    obj = LibrarySchemaEntity187Create(
        entity_code="TEST_LIBRARY_187",
        name="Test Entity 187",
        value_amount=187 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_187"
    assert obj.value_amount == 187 * 100.5

def test_library_entity_188_schema_validation():
    obj = LibrarySchemaEntity188Create(
        entity_code="TEST_LIBRARY_188",
        name="Test Entity 188",
        value_amount=188 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_188"
    assert obj.value_amount == 188 * 100.5

def test_library_entity_189_schema_validation():
    obj = LibrarySchemaEntity189Create(
        entity_code="TEST_LIBRARY_189",
        name="Test Entity 189",
        value_amount=189 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_189"
    assert obj.value_amount == 189 * 100.5

def test_library_entity_190_schema_validation():
    obj = LibrarySchemaEntity190Create(
        entity_code="TEST_LIBRARY_190",
        name="Test Entity 190",
        value_amount=190 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_190"
    assert obj.value_amount == 190 * 100.5

def test_library_entity_191_schema_validation():
    obj = LibrarySchemaEntity191Create(
        entity_code="TEST_LIBRARY_191",
        name="Test Entity 191",
        value_amount=191 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_191"
    assert obj.value_amount == 191 * 100.5

def test_library_entity_192_schema_validation():
    obj = LibrarySchemaEntity192Create(
        entity_code="TEST_LIBRARY_192",
        name="Test Entity 192",
        value_amount=192 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_192"
    assert obj.value_amount == 192 * 100.5

def test_library_entity_193_schema_validation():
    obj = LibrarySchemaEntity193Create(
        entity_code="TEST_LIBRARY_193",
        name="Test Entity 193",
        value_amount=193 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_193"
    assert obj.value_amount == 193 * 100.5

def test_library_entity_194_schema_validation():
    obj = LibrarySchemaEntity194Create(
        entity_code="TEST_LIBRARY_194",
        name="Test Entity 194",
        value_amount=194 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_194"
    assert obj.value_amount == 194 * 100.5

def test_library_entity_195_schema_validation():
    obj = LibrarySchemaEntity195Create(
        entity_code="TEST_LIBRARY_195",
        name="Test Entity 195",
        value_amount=195 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_195"
    assert obj.value_amount == 195 * 100.5

def test_library_entity_196_schema_validation():
    obj = LibrarySchemaEntity196Create(
        entity_code="TEST_LIBRARY_196",
        name="Test Entity 196",
        value_amount=196 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_196"
    assert obj.value_amount == 196 * 100.5

def test_library_entity_197_schema_validation():
    obj = LibrarySchemaEntity197Create(
        entity_code="TEST_LIBRARY_197",
        name="Test Entity 197",
        value_amount=197 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_197"
    assert obj.value_amount == 197 * 100.5

def test_library_entity_198_schema_validation():
    obj = LibrarySchemaEntity198Create(
        entity_code="TEST_LIBRARY_198",
        name="Test Entity 198",
        value_amount=198 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_198"
    assert obj.value_amount == 198 * 100.5

def test_library_entity_199_schema_validation():
    obj = LibrarySchemaEntity199Create(
        entity_code="TEST_LIBRARY_199",
        name="Test Entity 199",
        value_amount=199 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_199"
    assert obj.value_amount == 199 * 100.5

def test_library_entity_200_schema_validation():
    obj = LibrarySchemaEntity200Create(
        entity_code="TEST_LIBRARY_200",
        name="Test Entity 200",
        value_amount=200 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_200"
    assert obj.value_amount == 200 * 100.5

def test_library_entity_201_schema_validation():
    obj = LibrarySchemaEntity201Create(
        entity_code="TEST_LIBRARY_201",
        name="Test Entity 201",
        value_amount=201 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_201"
    assert obj.value_amount == 201 * 100.5

def test_library_entity_202_schema_validation():
    obj = LibrarySchemaEntity202Create(
        entity_code="TEST_LIBRARY_202",
        name="Test Entity 202",
        value_amount=202 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_202"
    assert obj.value_amount == 202 * 100.5

def test_library_entity_203_schema_validation():
    obj = LibrarySchemaEntity203Create(
        entity_code="TEST_LIBRARY_203",
        name="Test Entity 203",
        value_amount=203 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_203"
    assert obj.value_amount == 203 * 100.5

def test_library_entity_204_schema_validation():
    obj = LibrarySchemaEntity204Create(
        entity_code="TEST_LIBRARY_204",
        name="Test Entity 204",
        value_amount=204 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_204"
    assert obj.value_amount == 204 * 100.5

def test_library_entity_205_schema_validation():
    obj = LibrarySchemaEntity205Create(
        entity_code="TEST_LIBRARY_205",
        name="Test Entity 205",
        value_amount=205 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_205"
    assert obj.value_amount == 205 * 100.5

def test_library_entity_206_schema_validation():
    obj = LibrarySchemaEntity206Create(
        entity_code="TEST_LIBRARY_206",
        name="Test Entity 206",
        value_amount=206 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_206"
    assert obj.value_amount == 206 * 100.5

def test_library_entity_207_schema_validation():
    obj = LibrarySchemaEntity207Create(
        entity_code="TEST_LIBRARY_207",
        name="Test Entity 207",
        value_amount=207 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_207"
    assert obj.value_amount == 207 * 100.5

def test_library_entity_208_schema_validation():
    obj = LibrarySchemaEntity208Create(
        entity_code="TEST_LIBRARY_208",
        name="Test Entity 208",
        value_amount=208 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_208"
    assert obj.value_amount == 208 * 100.5

def test_library_entity_209_schema_validation():
    obj = LibrarySchemaEntity209Create(
        entity_code="TEST_LIBRARY_209",
        name="Test Entity 209",
        value_amount=209 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_209"
    assert obj.value_amount == 209 * 100.5

def test_library_entity_210_schema_validation():
    obj = LibrarySchemaEntity210Create(
        entity_code="TEST_LIBRARY_210",
        name="Test Entity 210",
        value_amount=210 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_210"
    assert obj.value_amount == 210 * 100.5

def test_library_entity_211_schema_validation():
    obj = LibrarySchemaEntity211Create(
        entity_code="TEST_LIBRARY_211",
        name="Test Entity 211",
        value_amount=211 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_211"
    assert obj.value_amount == 211 * 100.5

def test_library_entity_212_schema_validation():
    obj = LibrarySchemaEntity212Create(
        entity_code="TEST_LIBRARY_212",
        name="Test Entity 212",
        value_amount=212 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_212"
    assert obj.value_amount == 212 * 100.5

def test_library_entity_213_schema_validation():
    obj = LibrarySchemaEntity213Create(
        entity_code="TEST_LIBRARY_213",
        name="Test Entity 213",
        value_amount=213 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_213"
    assert obj.value_amount == 213 * 100.5

def test_library_entity_214_schema_validation():
    obj = LibrarySchemaEntity214Create(
        entity_code="TEST_LIBRARY_214",
        name="Test Entity 214",
        value_amount=214 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_214"
    assert obj.value_amount == 214 * 100.5

def test_library_entity_215_schema_validation():
    obj = LibrarySchemaEntity215Create(
        entity_code="TEST_LIBRARY_215",
        name="Test Entity 215",
        value_amount=215 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_215"
    assert obj.value_amount == 215 * 100.5

def test_library_entity_216_schema_validation():
    obj = LibrarySchemaEntity216Create(
        entity_code="TEST_LIBRARY_216",
        name="Test Entity 216",
        value_amount=216 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_216"
    assert obj.value_amount == 216 * 100.5

def test_library_entity_217_schema_validation():
    obj = LibrarySchemaEntity217Create(
        entity_code="TEST_LIBRARY_217",
        name="Test Entity 217",
        value_amount=217 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_217"
    assert obj.value_amount == 217 * 100.5

def test_library_entity_218_schema_validation():
    obj = LibrarySchemaEntity218Create(
        entity_code="TEST_LIBRARY_218",
        name="Test Entity 218",
        value_amount=218 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_218"
    assert obj.value_amount == 218 * 100.5

def test_library_entity_219_schema_validation():
    obj = LibrarySchemaEntity219Create(
        entity_code="TEST_LIBRARY_219",
        name="Test Entity 219",
        value_amount=219 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_219"
    assert obj.value_amount == 219 * 100.5

def test_library_entity_220_schema_validation():
    obj = LibrarySchemaEntity220Create(
        entity_code="TEST_LIBRARY_220",
        name="Test Entity 220",
        value_amount=220 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_220"
    assert obj.value_amount == 220 * 100.5

def test_library_entity_221_schema_validation():
    obj = LibrarySchemaEntity221Create(
        entity_code="TEST_LIBRARY_221",
        name="Test Entity 221",
        value_amount=221 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_221"
    assert obj.value_amount == 221 * 100.5

def test_library_entity_222_schema_validation():
    obj = LibrarySchemaEntity222Create(
        entity_code="TEST_LIBRARY_222",
        name="Test Entity 222",
        value_amount=222 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_222"
    assert obj.value_amount == 222 * 100.5

def test_library_entity_223_schema_validation():
    obj = LibrarySchemaEntity223Create(
        entity_code="TEST_LIBRARY_223",
        name="Test Entity 223",
        value_amount=223 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_223"
    assert obj.value_amount == 223 * 100.5

def test_library_entity_224_schema_validation():
    obj = LibrarySchemaEntity224Create(
        entity_code="TEST_LIBRARY_224",
        name="Test Entity 224",
        value_amount=224 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_224"
    assert obj.value_amount == 224 * 100.5

def test_library_entity_225_schema_validation():
    obj = LibrarySchemaEntity225Create(
        entity_code="TEST_LIBRARY_225",
        name="Test Entity 225",
        value_amount=225 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_225"
    assert obj.value_amount == 225 * 100.5

def test_library_entity_226_schema_validation():
    obj = LibrarySchemaEntity226Create(
        entity_code="TEST_LIBRARY_226",
        name="Test Entity 226",
        value_amount=226 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_226"
    assert obj.value_amount == 226 * 100.5

def test_library_entity_227_schema_validation():
    obj = LibrarySchemaEntity227Create(
        entity_code="TEST_LIBRARY_227",
        name="Test Entity 227",
        value_amount=227 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_227"
    assert obj.value_amount == 227 * 100.5

def test_library_entity_228_schema_validation():
    obj = LibrarySchemaEntity228Create(
        entity_code="TEST_LIBRARY_228",
        name="Test Entity 228",
        value_amount=228 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_228"
    assert obj.value_amount == 228 * 100.5

def test_library_entity_229_schema_validation():
    obj = LibrarySchemaEntity229Create(
        entity_code="TEST_LIBRARY_229",
        name="Test Entity 229",
        value_amount=229 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_229"
    assert obj.value_amount == 229 * 100.5

def test_library_entity_230_schema_validation():
    obj = LibrarySchemaEntity230Create(
        entity_code="TEST_LIBRARY_230",
        name="Test Entity 230",
        value_amount=230 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_230"
    assert obj.value_amount == 230 * 100.5

def test_library_entity_231_schema_validation():
    obj = LibrarySchemaEntity231Create(
        entity_code="TEST_LIBRARY_231",
        name="Test Entity 231",
        value_amount=231 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_231"
    assert obj.value_amount == 231 * 100.5

def test_library_entity_232_schema_validation():
    obj = LibrarySchemaEntity232Create(
        entity_code="TEST_LIBRARY_232",
        name="Test Entity 232",
        value_amount=232 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_232"
    assert obj.value_amount == 232 * 100.5

def test_library_entity_233_schema_validation():
    obj = LibrarySchemaEntity233Create(
        entity_code="TEST_LIBRARY_233",
        name="Test Entity 233",
        value_amount=233 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_233"
    assert obj.value_amount == 233 * 100.5

def test_library_entity_234_schema_validation():
    obj = LibrarySchemaEntity234Create(
        entity_code="TEST_LIBRARY_234",
        name="Test Entity 234",
        value_amount=234 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_234"
    assert obj.value_amount == 234 * 100.5

def test_library_entity_235_schema_validation():
    obj = LibrarySchemaEntity235Create(
        entity_code="TEST_LIBRARY_235",
        name="Test Entity 235",
        value_amount=235 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_235"
    assert obj.value_amount == 235 * 100.5

def test_library_entity_236_schema_validation():
    obj = LibrarySchemaEntity236Create(
        entity_code="TEST_LIBRARY_236",
        name="Test Entity 236",
        value_amount=236 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_236"
    assert obj.value_amount == 236 * 100.5

def test_library_entity_237_schema_validation():
    obj = LibrarySchemaEntity237Create(
        entity_code="TEST_LIBRARY_237",
        name="Test Entity 237",
        value_amount=237 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_237"
    assert obj.value_amount == 237 * 100.5

def test_library_entity_238_schema_validation():
    obj = LibrarySchemaEntity238Create(
        entity_code="TEST_LIBRARY_238",
        name="Test Entity 238",
        value_amount=238 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_238"
    assert obj.value_amount == 238 * 100.5

def test_library_entity_239_schema_validation():
    obj = LibrarySchemaEntity239Create(
        entity_code="TEST_LIBRARY_239",
        name="Test Entity 239",
        value_amount=239 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_239"
    assert obj.value_amount == 239 * 100.5

def test_library_entity_240_schema_validation():
    obj = LibrarySchemaEntity240Create(
        entity_code="TEST_LIBRARY_240",
        name="Test Entity 240",
        value_amount=240 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_240"
    assert obj.value_amount == 240 * 100.5

def test_library_entity_241_schema_validation():
    obj = LibrarySchemaEntity241Create(
        entity_code="TEST_LIBRARY_241",
        name="Test Entity 241",
        value_amount=241 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_241"
    assert obj.value_amount == 241 * 100.5

def test_library_entity_242_schema_validation():
    obj = LibrarySchemaEntity242Create(
        entity_code="TEST_LIBRARY_242",
        name="Test Entity 242",
        value_amount=242 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_242"
    assert obj.value_amount == 242 * 100.5

def test_library_entity_243_schema_validation():
    obj = LibrarySchemaEntity243Create(
        entity_code="TEST_LIBRARY_243",
        name="Test Entity 243",
        value_amount=243 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_243"
    assert obj.value_amount == 243 * 100.5

def test_library_entity_244_schema_validation():
    obj = LibrarySchemaEntity244Create(
        entity_code="TEST_LIBRARY_244",
        name="Test Entity 244",
        value_amount=244 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_244"
    assert obj.value_amount == 244 * 100.5

def test_library_entity_245_schema_validation():
    obj = LibrarySchemaEntity245Create(
        entity_code="TEST_LIBRARY_245",
        name="Test Entity 245",
        value_amount=245 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_245"
    assert obj.value_amount == 245 * 100.5

def test_library_entity_246_schema_validation():
    obj = LibrarySchemaEntity246Create(
        entity_code="TEST_LIBRARY_246",
        name="Test Entity 246",
        value_amount=246 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_246"
    assert obj.value_amount == 246 * 100.5

def test_library_entity_247_schema_validation():
    obj = LibrarySchemaEntity247Create(
        entity_code="TEST_LIBRARY_247",
        name="Test Entity 247",
        value_amount=247 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_247"
    assert obj.value_amount == 247 * 100.5

def test_library_entity_248_schema_validation():
    obj = LibrarySchemaEntity248Create(
        entity_code="TEST_LIBRARY_248",
        name="Test Entity 248",
        value_amount=248 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_248"
    assert obj.value_amount == 248 * 100.5

def test_library_entity_249_schema_validation():
    obj = LibrarySchemaEntity249Create(
        entity_code="TEST_LIBRARY_249",
        name="Test Entity 249",
        value_amount=249 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_249"
    assert obj.value_amount == 249 * 100.5

def test_library_entity_250_schema_validation():
    obj = LibrarySchemaEntity250Create(
        entity_code="TEST_LIBRARY_250",
        name="Test Entity 250",
        value_amount=250 * 100.5
    )
    assert obj.entity_code == "TEST_LIBRARY_250"
    assert obj.value_amount == 250 * 100.5


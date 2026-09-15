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


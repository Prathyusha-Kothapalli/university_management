"""
Pytest suite for Sports & Extracurricular Activities
"""
import pytest
from app.domains.sports.schemas import *

def test_sports_entity_1_schema_validation():
    obj = SportsSchemaEntity1Create(
        entity_code="TEST_SPORTS_1",
        name="Test Entity 1",
        value_amount=1 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_1"
    assert obj.value_amount == 1 * 100.5

def test_sports_entity_2_schema_validation():
    obj = SportsSchemaEntity2Create(
        entity_code="TEST_SPORTS_2",
        name="Test Entity 2",
        value_amount=2 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_2"
    assert obj.value_amount == 2 * 100.5

def test_sports_entity_3_schema_validation():
    obj = SportsSchemaEntity3Create(
        entity_code="TEST_SPORTS_3",
        name="Test Entity 3",
        value_amount=3 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_3"
    assert obj.value_amount == 3 * 100.5

def test_sports_entity_4_schema_validation():
    obj = SportsSchemaEntity4Create(
        entity_code="TEST_SPORTS_4",
        name="Test Entity 4",
        value_amount=4 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_4"
    assert obj.value_amount == 4 * 100.5

def test_sports_entity_5_schema_validation():
    obj = SportsSchemaEntity5Create(
        entity_code="TEST_SPORTS_5",
        name="Test Entity 5",
        value_amount=5 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_5"
    assert obj.value_amount == 5 * 100.5

def test_sports_entity_6_schema_validation():
    obj = SportsSchemaEntity6Create(
        entity_code="TEST_SPORTS_6",
        name="Test Entity 6",
        value_amount=6 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_6"
    assert obj.value_amount == 6 * 100.5

def test_sports_entity_7_schema_validation():
    obj = SportsSchemaEntity7Create(
        entity_code="TEST_SPORTS_7",
        name="Test Entity 7",
        value_amount=7 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_7"
    assert obj.value_amount == 7 * 100.5

def test_sports_entity_8_schema_validation():
    obj = SportsSchemaEntity8Create(
        entity_code="TEST_SPORTS_8",
        name="Test Entity 8",
        value_amount=8 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_8"
    assert obj.value_amount == 8 * 100.5

def test_sports_entity_9_schema_validation():
    obj = SportsSchemaEntity9Create(
        entity_code="TEST_SPORTS_9",
        name="Test Entity 9",
        value_amount=9 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_9"
    assert obj.value_amount == 9 * 100.5

def test_sports_entity_10_schema_validation():
    obj = SportsSchemaEntity10Create(
        entity_code="TEST_SPORTS_10",
        name="Test Entity 10",
        value_amount=10 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_10"
    assert obj.value_amount == 10 * 100.5

def test_sports_entity_11_schema_validation():
    obj = SportsSchemaEntity11Create(
        entity_code="TEST_SPORTS_11",
        name="Test Entity 11",
        value_amount=11 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_11"
    assert obj.value_amount == 11 * 100.5

def test_sports_entity_12_schema_validation():
    obj = SportsSchemaEntity12Create(
        entity_code="TEST_SPORTS_12",
        name="Test Entity 12",
        value_amount=12 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_12"
    assert obj.value_amount == 12 * 100.5

def test_sports_entity_13_schema_validation():
    obj = SportsSchemaEntity13Create(
        entity_code="TEST_SPORTS_13",
        name="Test Entity 13",
        value_amount=13 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_13"
    assert obj.value_amount == 13 * 100.5

def test_sports_entity_14_schema_validation():
    obj = SportsSchemaEntity14Create(
        entity_code="TEST_SPORTS_14",
        name="Test Entity 14",
        value_amount=14 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_14"
    assert obj.value_amount == 14 * 100.5

def test_sports_entity_15_schema_validation():
    obj = SportsSchemaEntity15Create(
        entity_code="TEST_SPORTS_15",
        name="Test Entity 15",
        value_amount=15 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_15"
    assert obj.value_amount == 15 * 100.5

def test_sports_entity_16_schema_validation():
    obj = SportsSchemaEntity16Create(
        entity_code="TEST_SPORTS_16",
        name="Test Entity 16",
        value_amount=16 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_16"
    assert obj.value_amount == 16 * 100.5

def test_sports_entity_17_schema_validation():
    obj = SportsSchemaEntity17Create(
        entity_code="TEST_SPORTS_17",
        name="Test Entity 17",
        value_amount=17 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_17"
    assert obj.value_amount == 17 * 100.5

def test_sports_entity_18_schema_validation():
    obj = SportsSchemaEntity18Create(
        entity_code="TEST_SPORTS_18",
        name="Test Entity 18",
        value_amount=18 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_18"
    assert obj.value_amount == 18 * 100.5

def test_sports_entity_19_schema_validation():
    obj = SportsSchemaEntity19Create(
        entity_code="TEST_SPORTS_19",
        name="Test Entity 19",
        value_amount=19 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_19"
    assert obj.value_amount == 19 * 100.5

def test_sports_entity_20_schema_validation():
    obj = SportsSchemaEntity20Create(
        entity_code="TEST_SPORTS_20",
        name="Test Entity 20",
        value_amount=20 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_20"
    assert obj.value_amount == 20 * 100.5

def test_sports_entity_21_schema_validation():
    obj = SportsSchemaEntity21Create(
        entity_code="TEST_SPORTS_21",
        name="Test Entity 21",
        value_amount=21 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_21"
    assert obj.value_amount == 21 * 100.5

def test_sports_entity_22_schema_validation():
    obj = SportsSchemaEntity22Create(
        entity_code="TEST_SPORTS_22",
        name="Test Entity 22",
        value_amount=22 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_22"
    assert obj.value_amount == 22 * 100.5

def test_sports_entity_23_schema_validation():
    obj = SportsSchemaEntity23Create(
        entity_code="TEST_SPORTS_23",
        name="Test Entity 23",
        value_amount=23 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_23"
    assert obj.value_amount == 23 * 100.5

def test_sports_entity_24_schema_validation():
    obj = SportsSchemaEntity24Create(
        entity_code="TEST_SPORTS_24",
        name="Test Entity 24",
        value_amount=24 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_24"
    assert obj.value_amount == 24 * 100.5

def test_sports_entity_25_schema_validation():
    obj = SportsSchemaEntity25Create(
        entity_code="TEST_SPORTS_25",
        name="Test Entity 25",
        value_amount=25 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_25"
    assert obj.value_amount == 25 * 100.5

def test_sports_entity_26_schema_validation():
    obj = SportsSchemaEntity26Create(
        entity_code="TEST_SPORTS_26",
        name="Test Entity 26",
        value_amount=26 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_26"
    assert obj.value_amount == 26 * 100.5

def test_sports_entity_27_schema_validation():
    obj = SportsSchemaEntity27Create(
        entity_code="TEST_SPORTS_27",
        name="Test Entity 27",
        value_amount=27 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_27"
    assert obj.value_amount == 27 * 100.5

def test_sports_entity_28_schema_validation():
    obj = SportsSchemaEntity28Create(
        entity_code="TEST_SPORTS_28",
        name="Test Entity 28",
        value_amount=28 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_28"
    assert obj.value_amount == 28 * 100.5

def test_sports_entity_29_schema_validation():
    obj = SportsSchemaEntity29Create(
        entity_code="TEST_SPORTS_29",
        name="Test Entity 29",
        value_amount=29 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_29"
    assert obj.value_amount == 29 * 100.5

def test_sports_entity_30_schema_validation():
    obj = SportsSchemaEntity30Create(
        entity_code="TEST_SPORTS_30",
        name="Test Entity 30",
        value_amount=30 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_30"
    assert obj.value_amount == 30 * 100.5

def test_sports_entity_31_schema_validation():
    obj = SportsSchemaEntity31Create(
        entity_code="TEST_SPORTS_31",
        name="Test Entity 31",
        value_amount=31 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_31"
    assert obj.value_amount == 31 * 100.5

def test_sports_entity_32_schema_validation():
    obj = SportsSchemaEntity32Create(
        entity_code="TEST_SPORTS_32",
        name="Test Entity 32",
        value_amount=32 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_32"
    assert obj.value_amount == 32 * 100.5

def test_sports_entity_33_schema_validation():
    obj = SportsSchemaEntity33Create(
        entity_code="TEST_SPORTS_33",
        name="Test Entity 33",
        value_amount=33 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_33"
    assert obj.value_amount == 33 * 100.5

def test_sports_entity_34_schema_validation():
    obj = SportsSchemaEntity34Create(
        entity_code="TEST_SPORTS_34",
        name="Test Entity 34",
        value_amount=34 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_34"
    assert obj.value_amount == 34 * 100.5

def test_sports_entity_35_schema_validation():
    obj = SportsSchemaEntity35Create(
        entity_code="TEST_SPORTS_35",
        name="Test Entity 35",
        value_amount=35 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_35"
    assert obj.value_amount == 35 * 100.5

def test_sports_entity_36_schema_validation():
    obj = SportsSchemaEntity36Create(
        entity_code="TEST_SPORTS_36",
        name="Test Entity 36",
        value_amount=36 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_36"
    assert obj.value_amount == 36 * 100.5

def test_sports_entity_37_schema_validation():
    obj = SportsSchemaEntity37Create(
        entity_code="TEST_SPORTS_37",
        name="Test Entity 37",
        value_amount=37 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_37"
    assert obj.value_amount == 37 * 100.5

def test_sports_entity_38_schema_validation():
    obj = SportsSchemaEntity38Create(
        entity_code="TEST_SPORTS_38",
        name="Test Entity 38",
        value_amount=38 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_38"
    assert obj.value_amount == 38 * 100.5

def test_sports_entity_39_schema_validation():
    obj = SportsSchemaEntity39Create(
        entity_code="TEST_SPORTS_39",
        name="Test Entity 39",
        value_amount=39 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_39"
    assert obj.value_amount == 39 * 100.5

def test_sports_entity_40_schema_validation():
    obj = SportsSchemaEntity40Create(
        entity_code="TEST_SPORTS_40",
        name="Test Entity 40",
        value_amount=40 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_40"
    assert obj.value_amount == 40 * 100.5

def test_sports_entity_41_schema_validation():
    obj = SportsSchemaEntity41Create(
        entity_code="TEST_SPORTS_41",
        name="Test Entity 41",
        value_amount=41 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_41"
    assert obj.value_amount == 41 * 100.5

def test_sports_entity_42_schema_validation():
    obj = SportsSchemaEntity42Create(
        entity_code="TEST_SPORTS_42",
        name="Test Entity 42",
        value_amount=42 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_42"
    assert obj.value_amount == 42 * 100.5

def test_sports_entity_43_schema_validation():
    obj = SportsSchemaEntity43Create(
        entity_code="TEST_SPORTS_43",
        name="Test Entity 43",
        value_amount=43 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_43"
    assert obj.value_amount == 43 * 100.5

def test_sports_entity_44_schema_validation():
    obj = SportsSchemaEntity44Create(
        entity_code="TEST_SPORTS_44",
        name="Test Entity 44",
        value_amount=44 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_44"
    assert obj.value_amount == 44 * 100.5

def test_sports_entity_45_schema_validation():
    obj = SportsSchemaEntity45Create(
        entity_code="TEST_SPORTS_45",
        name="Test Entity 45",
        value_amount=45 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_45"
    assert obj.value_amount == 45 * 100.5

def test_sports_entity_46_schema_validation():
    obj = SportsSchemaEntity46Create(
        entity_code="TEST_SPORTS_46",
        name="Test Entity 46",
        value_amount=46 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_46"
    assert obj.value_amount == 46 * 100.5

def test_sports_entity_47_schema_validation():
    obj = SportsSchemaEntity47Create(
        entity_code="TEST_SPORTS_47",
        name="Test Entity 47",
        value_amount=47 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_47"
    assert obj.value_amount == 47 * 100.5

def test_sports_entity_48_schema_validation():
    obj = SportsSchemaEntity48Create(
        entity_code="TEST_SPORTS_48",
        name="Test Entity 48",
        value_amount=48 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_48"
    assert obj.value_amount == 48 * 100.5

def test_sports_entity_49_schema_validation():
    obj = SportsSchemaEntity49Create(
        entity_code="TEST_SPORTS_49",
        name="Test Entity 49",
        value_amount=49 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_49"
    assert obj.value_amount == 49 * 100.5

def test_sports_entity_50_schema_validation():
    obj = SportsSchemaEntity50Create(
        entity_code="TEST_SPORTS_50",
        name="Test Entity 50",
        value_amount=50 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_50"
    assert obj.value_amount == 50 * 100.5

def test_sports_entity_51_schema_validation():
    obj = SportsSchemaEntity51Create(
        entity_code="TEST_SPORTS_51",
        name="Test Entity 51",
        value_amount=51 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_51"
    assert obj.value_amount == 51 * 100.5

def test_sports_entity_52_schema_validation():
    obj = SportsSchemaEntity52Create(
        entity_code="TEST_SPORTS_52",
        name="Test Entity 52",
        value_amount=52 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_52"
    assert obj.value_amount == 52 * 100.5

def test_sports_entity_53_schema_validation():
    obj = SportsSchemaEntity53Create(
        entity_code="TEST_SPORTS_53",
        name="Test Entity 53",
        value_amount=53 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_53"
    assert obj.value_amount == 53 * 100.5

def test_sports_entity_54_schema_validation():
    obj = SportsSchemaEntity54Create(
        entity_code="TEST_SPORTS_54",
        name="Test Entity 54",
        value_amount=54 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_54"
    assert obj.value_amount == 54 * 100.5

def test_sports_entity_55_schema_validation():
    obj = SportsSchemaEntity55Create(
        entity_code="TEST_SPORTS_55",
        name="Test Entity 55",
        value_amount=55 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_55"
    assert obj.value_amount == 55 * 100.5

def test_sports_entity_56_schema_validation():
    obj = SportsSchemaEntity56Create(
        entity_code="TEST_SPORTS_56",
        name="Test Entity 56",
        value_amount=56 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_56"
    assert obj.value_amount == 56 * 100.5

def test_sports_entity_57_schema_validation():
    obj = SportsSchemaEntity57Create(
        entity_code="TEST_SPORTS_57",
        name="Test Entity 57",
        value_amount=57 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_57"
    assert obj.value_amount == 57 * 100.5

def test_sports_entity_58_schema_validation():
    obj = SportsSchemaEntity58Create(
        entity_code="TEST_SPORTS_58",
        name="Test Entity 58",
        value_amount=58 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_58"
    assert obj.value_amount == 58 * 100.5

def test_sports_entity_59_schema_validation():
    obj = SportsSchemaEntity59Create(
        entity_code="TEST_SPORTS_59",
        name="Test Entity 59",
        value_amount=59 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_59"
    assert obj.value_amount == 59 * 100.5

def test_sports_entity_60_schema_validation():
    obj = SportsSchemaEntity60Create(
        entity_code="TEST_SPORTS_60",
        name="Test Entity 60",
        value_amount=60 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_60"
    assert obj.value_amount == 60 * 100.5

def test_sports_entity_61_schema_validation():
    obj = SportsSchemaEntity61Create(
        entity_code="TEST_SPORTS_61",
        name="Test Entity 61",
        value_amount=61 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_61"
    assert obj.value_amount == 61 * 100.5

def test_sports_entity_62_schema_validation():
    obj = SportsSchemaEntity62Create(
        entity_code="TEST_SPORTS_62",
        name="Test Entity 62",
        value_amount=62 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_62"
    assert obj.value_amount == 62 * 100.5

def test_sports_entity_63_schema_validation():
    obj = SportsSchemaEntity63Create(
        entity_code="TEST_SPORTS_63",
        name="Test Entity 63",
        value_amount=63 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_63"
    assert obj.value_amount == 63 * 100.5

def test_sports_entity_64_schema_validation():
    obj = SportsSchemaEntity64Create(
        entity_code="TEST_SPORTS_64",
        name="Test Entity 64",
        value_amount=64 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_64"
    assert obj.value_amount == 64 * 100.5

def test_sports_entity_65_schema_validation():
    obj = SportsSchemaEntity65Create(
        entity_code="TEST_SPORTS_65",
        name="Test Entity 65",
        value_amount=65 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_65"
    assert obj.value_amount == 65 * 100.5

def test_sports_entity_66_schema_validation():
    obj = SportsSchemaEntity66Create(
        entity_code="TEST_SPORTS_66",
        name="Test Entity 66",
        value_amount=66 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_66"
    assert obj.value_amount == 66 * 100.5

def test_sports_entity_67_schema_validation():
    obj = SportsSchemaEntity67Create(
        entity_code="TEST_SPORTS_67",
        name="Test Entity 67",
        value_amount=67 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_67"
    assert obj.value_amount == 67 * 100.5

def test_sports_entity_68_schema_validation():
    obj = SportsSchemaEntity68Create(
        entity_code="TEST_SPORTS_68",
        name="Test Entity 68",
        value_amount=68 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_68"
    assert obj.value_amount == 68 * 100.5

def test_sports_entity_69_schema_validation():
    obj = SportsSchemaEntity69Create(
        entity_code="TEST_SPORTS_69",
        name="Test Entity 69",
        value_amount=69 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_69"
    assert obj.value_amount == 69 * 100.5

def test_sports_entity_70_schema_validation():
    obj = SportsSchemaEntity70Create(
        entity_code="TEST_SPORTS_70",
        name="Test Entity 70",
        value_amount=70 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_70"
    assert obj.value_amount == 70 * 100.5

def test_sports_entity_71_schema_validation():
    obj = SportsSchemaEntity71Create(
        entity_code="TEST_SPORTS_71",
        name="Test Entity 71",
        value_amount=71 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_71"
    assert obj.value_amount == 71 * 100.5

def test_sports_entity_72_schema_validation():
    obj = SportsSchemaEntity72Create(
        entity_code="TEST_SPORTS_72",
        name="Test Entity 72",
        value_amount=72 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_72"
    assert obj.value_amount == 72 * 100.5

def test_sports_entity_73_schema_validation():
    obj = SportsSchemaEntity73Create(
        entity_code="TEST_SPORTS_73",
        name="Test Entity 73",
        value_amount=73 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_73"
    assert obj.value_amount == 73 * 100.5

def test_sports_entity_74_schema_validation():
    obj = SportsSchemaEntity74Create(
        entity_code="TEST_SPORTS_74",
        name="Test Entity 74",
        value_amount=74 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_74"
    assert obj.value_amount == 74 * 100.5

def test_sports_entity_75_schema_validation():
    obj = SportsSchemaEntity75Create(
        entity_code="TEST_SPORTS_75",
        name="Test Entity 75",
        value_amount=75 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_75"
    assert obj.value_amount == 75 * 100.5

def test_sports_entity_76_schema_validation():
    obj = SportsSchemaEntity76Create(
        entity_code="TEST_SPORTS_76",
        name="Test Entity 76",
        value_amount=76 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_76"
    assert obj.value_amount == 76 * 100.5

def test_sports_entity_77_schema_validation():
    obj = SportsSchemaEntity77Create(
        entity_code="TEST_SPORTS_77",
        name="Test Entity 77",
        value_amount=77 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_77"
    assert obj.value_amount == 77 * 100.5

def test_sports_entity_78_schema_validation():
    obj = SportsSchemaEntity78Create(
        entity_code="TEST_SPORTS_78",
        name="Test Entity 78",
        value_amount=78 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_78"
    assert obj.value_amount == 78 * 100.5

def test_sports_entity_79_schema_validation():
    obj = SportsSchemaEntity79Create(
        entity_code="TEST_SPORTS_79",
        name="Test Entity 79",
        value_amount=79 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_79"
    assert obj.value_amount == 79 * 100.5

def test_sports_entity_80_schema_validation():
    obj = SportsSchemaEntity80Create(
        entity_code="TEST_SPORTS_80",
        name="Test Entity 80",
        value_amount=80 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_80"
    assert obj.value_amount == 80 * 100.5

def test_sports_entity_81_schema_validation():
    obj = SportsSchemaEntity81Create(
        entity_code="TEST_SPORTS_81",
        name="Test Entity 81",
        value_amount=81 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_81"
    assert obj.value_amount == 81 * 100.5

def test_sports_entity_82_schema_validation():
    obj = SportsSchemaEntity82Create(
        entity_code="TEST_SPORTS_82",
        name="Test Entity 82",
        value_amount=82 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_82"
    assert obj.value_amount == 82 * 100.5

def test_sports_entity_83_schema_validation():
    obj = SportsSchemaEntity83Create(
        entity_code="TEST_SPORTS_83",
        name="Test Entity 83",
        value_amount=83 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_83"
    assert obj.value_amount == 83 * 100.5

def test_sports_entity_84_schema_validation():
    obj = SportsSchemaEntity84Create(
        entity_code="TEST_SPORTS_84",
        name="Test Entity 84",
        value_amount=84 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_84"
    assert obj.value_amount == 84 * 100.5

def test_sports_entity_85_schema_validation():
    obj = SportsSchemaEntity85Create(
        entity_code="TEST_SPORTS_85",
        name="Test Entity 85",
        value_amount=85 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_85"
    assert obj.value_amount == 85 * 100.5

def test_sports_entity_86_schema_validation():
    obj = SportsSchemaEntity86Create(
        entity_code="TEST_SPORTS_86",
        name="Test Entity 86",
        value_amount=86 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_86"
    assert obj.value_amount == 86 * 100.5

def test_sports_entity_87_schema_validation():
    obj = SportsSchemaEntity87Create(
        entity_code="TEST_SPORTS_87",
        name="Test Entity 87",
        value_amount=87 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_87"
    assert obj.value_amount == 87 * 100.5

def test_sports_entity_88_schema_validation():
    obj = SportsSchemaEntity88Create(
        entity_code="TEST_SPORTS_88",
        name="Test Entity 88",
        value_amount=88 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_88"
    assert obj.value_amount == 88 * 100.5

def test_sports_entity_89_schema_validation():
    obj = SportsSchemaEntity89Create(
        entity_code="TEST_SPORTS_89",
        name="Test Entity 89",
        value_amount=89 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_89"
    assert obj.value_amount == 89 * 100.5

def test_sports_entity_90_schema_validation():
    obj = SportsSchemaEntity90Create(
        entity_code="TEST_SPORTS_90",
        name="Test Entity 90",
        value_amount=90 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_90"
    assert obj.value_amount == 90 * 100.5

def test_sports_entity_91_schema_validation():
    obj = SportsSchemaEntity91Create(
        entity_code="TEST_SPORTS_91",
        name="Test Entity 91",
        value_amount=91 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_91"
    assert obj.value_amount == 91 * 100.5

def test_sports_entity_92_schema_validation():
    obj = SportsSchemaEntity92Create(
        entity_code="TEST_SPORTS_92",
        name="Test Entity 92",
        value_amount=92 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_92"
    assert obj.value_amount == 92 * 100.5

def test_sports_entity_93_schema_validation():
    obj = SportsSchemaEntity93Create(
        entity_code="TEST_SPORTS_93",
        name="Test Entity 93",
        value_amount=93 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_93"
    assert obj.value_amount == 93 * 100.5

def test_sports_entity_94_schema_validation():
    obj = SportsSchemaEntity94Create(
        entity_code="TEST_SPORTS_94",
        name="Test Entity 94",
        value_amount=94 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_94"
    assert obj.value_amount == 94 * 100.5

def test_sports_entity_95_schema_validation():
    obj = SportsSchemaEntity95Create(
        entity_code="TEST_SPORTS_95",
        name="Test Entity 95",
        value_amount=95 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_95"
    assert obj.value_amount == 95 * 100.5

def test_sports_entity_96_schema_validation():
    obj = SportsSchemaEntity96Create(
        entity_code="TEST_SPORTS_96",
        name="Test Entity 96",
        value_amount=96 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_96"
    assert obj.value_amount == 96 * 100.5

def test_sports_entity_97_schema_validation():
    obj = SportsSchemaEntity97Create(
        entity_code="TEST_SPORTS_97",
        name="Test Entity 97",
        value_amount=97 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_97"
    assert obj.value_amount == 97 * 100.5

def test_sports_entity_98_schema_validation():
    obj = SportsSchemaEntity98Create(
        entity_code="TEST_SPORTS_98",
        name="Test Entity 98",
        value_amount=98 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_98"
    assert obj.value_amount == 98 * 100.5

def test_sports_entity_99_schema_validation():
    obj = SportsSchemaEntity99Create(
        entity_code="TEST_SPORTS_99",
        name="Test Entity 99",
        value_amount=99 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_99"
    assert obj.value_amount == 99 * 100.5

def test_sports_entity_100_schema_validation():
    obj = SportsSchemaEntity100Create(
        entity_code="TEST_SPORTS_100",
        name="Test Entity 100",
        value_amount=100 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_100"
    assert obj.value_amount == 100 * 100.5

def test_sports_entity_101_schema_validation():
    obj = SportsSchemaEntity101Create(
        entity_code="TEST_SPORTS_101",
        name="Test Entity 101",
        value_amount=101 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_101"
    assert obj.value_amount == 101 * 100.5

def test_sports_entity_102_schema_validation():
    obj = SportsSchemaEntity102Create(
        entity_code="TEST_SPORTS_102",
        name="Test Entity 102",
        value_amount=102 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_102"
    assert obj.value_amount == 102 * 100.5

def test_sports_entity_103_schema_validation():
    obj = SportsSchemaEntity103Create(
        entity_code="TEST_SPORTS_103",
        name="Test Entity 103",
        value_amount=103 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_103"
    assert obj.value_amount == 103 * 100.5

def test_sports_entity_104_schema_validation():
    obj = SportsSchemaEntity104Create(
        entity_code="TEST_SPORTS_104",
        name="Test Entity 104",
        value_amount=104 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_104"
    assert obj.value_amount == 104 * 100.5

def test_sports_entity_105_schema_validation():
    obj = SportsSchemaEntity105Create(
        entity_code="TEST_SPORTS_105",
        name="Test Entity 105",
        value_amount=105 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_105"
    assert obj.value_amount == 105 * 100.5

def test_sports_entity_106_schema_validation():
    obj = SportsSchemaEntity106Create(
        entity_code="TEST_SPORTS_106",
        name="Test Entity 106",
        value_amount=106 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_106"
    assert obj.value_amount == 106 * 100.5

def test_sports_entity_107_schema_validation():
    obj = SportsSchemaEntity107Create(
        entity_code="TEST_SPORTS_107",
        name="Test Entity 107",
        value_amount=107 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_107"
    assert obj.value_amount == 107 * 100.5

def test_sports_entity_108_schema_validation():
    obj = SportsSchemaEntity108Create(
        entity_code="TEST_SPORTS_108",
        name="Test Entity 108",
        value_amount=108 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_108"
    assert obj.value_amount == 108 * 100.5

def test_sports_entity_109_schema_validation():
    obj = SportsSchemaEntity109Create(
        entity_code="TEST_SPORTS_109",
        name="Test Entity 109",
        value_amount=109 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_109"
    assert obj.value_amount == 109 * 100.5

def test_sports_entity_110_schema_validation():
    obj = SportsSchemaEntity110Create(
        entity_code="TEST_SPORTS_110",
        name="Test Entity 110",
        value_amount=110 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_110"
    assert obj.value_amount == 110 * 100.5

def test_sports_entity_111_schema_validation():
    obj = SportsSchemaEntity111Create(
        entity_code="TEST_SPORTS_111",
        name="Test Entity 111",
        value_amount=111 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_111"
    assert obj.value_amount == 111 * 100.5

def test_sports_entity_112_schema_validation():
    obj = SportsSchemaEntity112Create(
        entity_code="TEST_SPORTS_112",
        name="Test Entity 112",
        value_amount=112 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_112"
    assert obj.value_amount == 112 * 100.5

def test_sports_entity_113_schema_validation():
    obj = SportsSchemaEntity113Create(
        entity_code="TEST_SPORTS_113",
        name="Test Entity 113",
        value_amount=113 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_113"
    assert obj.value_amount == 113 * 100.5

def test_sports_entity_114_schema_validation():
    obj = SportsSchemaEntity114Create(
        entity_code="TEST_SPORTS_114",
        name="Test Entity 114",
        value_amount=114 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_114"
    assert obj.value_amount == 114 * 100.5

def test_sports_entity_115_schema_validation():
    obj = SportsSchemaEntity115Create(
        entity_code="TEST_SPORTS_115",
        name="Test Entity 115",
        value_amount=115 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_115"
    assert obj.value_amount == 115 * 100.5

def test_sports_entity_116_schema_validation():
    obj = SportsSchemaEntity116Create(
        entity_code="TEST_SPORTS_116",
        name="Test Entity 116",
        value_amount=116 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_116"
    assert obj.value_amount == 116 * 100.5

def test_sports_entity_117_schema_validation():
    obj = SportsSchemaEntity117Create(
        entity_code="TEST_SPORTS_117",
        name="Test Entity 117",
        value_amount=117 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_117"
    assert obj.value_amount == 117 * 100.5

def test_sports_entity_118_schema_validation():
    obj = SportsSchemaEntity118Create(
        entity_code="TEST_SPORTS_118",
        name="Test Entity 118",
        value_amount=118 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_118"
    assert obj.value_amount == 118 * 100.5

def test_sports_entity_119_schema_validation():
    obj = SportsSchemaEntity119Create(
        entity_code="TEST_SPORTS_119",
        name="Test Entity 119",
        value_amount=119 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_119"
    assert obj.value_amount == 119 * 100.5

def test_sports_entity_120_schema_validation():
    obj = SportsSchemaEntity120Create(
        entity_code="TEST_SPORTS_120",
        name="Test Entity 120",
        value_amount=120 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_120"
    assert obj.value_amount == 120 * 100.5

def test_sports_entity_121_schema_validation():
    obj = SportsSchemaEntity121Create(
        entity_code="TEST_SPORTS_121",
        name="Test Entity 121",
        value_amount=121 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_121"
    assert obj.value_amount == 121 * 100.5

def test_sports_entity_122_schema_validation():
    obj = SportsSchemaEntity122Create(
        entity_code="TEST_SPORTS_122",
        name="Test Entity 122",
        value_amount=122 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_122"
    assert obj.value_amount == 122 * 100.5

def test_sports_entity_123_schema_validation():
    obj = SportsSchemaEntity123Create(
        entity_code="TEST_SPORTS_123",
        name="Test Entity 123",
        value_amount=123 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_123"
    assert obj.value_amount == 123 * 100.5

def test_sports_entity_124_schema_validation():
    obj = SportsSchemaEntity124Create(
        entity_code="TEST_SPORTS_124",
        name="Test Entity 124",
        value_amount=124 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_124"
    assert obj.value_amount == 124 * 100.5

def test_sports_entity_125_schema_validation():
    obj = SportsSchemaEntity125Create(
        entity_code="TEST_SPORTS_125",
        name="Test Entity 125",
        value_amount=125 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_125"
    assert obj.value_amount == 125 * 100.5

def test_sports_entity_126_schema_validation():
    obj = SportsSchemaEntity126Create(
        entity_code="TEST_SPORTS_126",
        name="Test Entity 126",
        value_amount=126 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_126"
    assert obj.value_amount == 126 * 100.5

def test_sports_entity_127_schema_validation():
    obj = SportsSchemaEntity127Create(
        entity_code="TEST_SPORTS_127",
        name="Test Entity 127",
        value_amount=127 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_127"
    assert obj.value_amount == 127 * 100.5

def test_sports_entity_128_schema_validation():
    obj = SportsSchemaEntity128Create(
        entity_code="TEST_SPORTS_128",
        name="Test Entity 128",
        value_amount=128 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_128"
    assert obj.value_amount == 128 * 100.5

def test_sports_entity_129_schema_validation():
    obj = SportsSchemaEntity129Create(
        entity_code="TEST_SPORTS_129",
        name="Test Entity 129",
        value_amount=129 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_129"
    assert obj.value_amount == 129 * 100.5

def test_sports_entity_130_schema_validation():
    obj = SportsSchemaEntity130Create(
        entity_code="TEST_SPORTS_130",
        name="Test Entity 130",
        value_amount=130 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_130"
    assert obj.value_amount == 130 * 100.5

def test_sports_entity_131_schema_validation():
    obj = SportsSchemaEntity131Create(
        entity_code="TEST_SPORTS_131",
        name="Test Entity 131",
        value_amount=131 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_131"
    assert obj.value_amount == 131 * 100.5

def test_sports_entity_132_schema_validation():
    obj = SportsSchemaEntity132Create(
        entity_code="TEST_SPORTS_132",
        name="Test Entity 132",
        value_amount=132 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_132"
    assert obj.value_amount == 132 * 100.5

def test_sports_entity_133_schema_validation():
    obj = SportsSchemaEntity133Create(
        entity_code="TEST_SPORTS_133",
        name="Test Entity 133",
        value_amount=133 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_133"
    assert obj.value_amount == 133 * 100.5

def test_sports_entity_134_schema_validation():
    obj = SportsSchemaEntity134Create(
        entity_code="TEST_SPORTS_134",
        name="Test Entity 134",
        value_amount=134 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_134"
    assert obj.value_amount == 134 * 100.5

def test_sports_entity_135_schema_validation():
    obj = SportsSchemaEntity135Create(
        entity_code="TEST_SPORTS_135",
        name="Test Entity 135",
        value_amount=135 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_135"
    assert obj.value_amount == 135 * 100.5

def test_sports_entity_136_schema_validation():
    obj = SportsSchemaEntity136Create(
        entity_code="TEST_SPORTS_136",
        name="Test Entity 136",
        value_amount=136 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_136"
    assert obj.value_amount == 136 * 100.5

def test_sports_entity_137_schema_validation():
    obj = SportsSchemaEntity137Create(
        entity_code="TEST_SPORTS_137",
        name="Test Entity 137",
        value_amount=137 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_137"
    assert obj.value_amount == 137 * 100.5

def test_sports_entity_138_schema_validation():
    obj = SportsSchemaEntity138Create(
        entity_code="TEST_SPORTS_138",
        name="Test Entity 138",
        value_amount=138 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_138"
    assert obj.value_amount == 138 * 100.5

def test_sports_entity_139_schema_validation():
    obj = SportsSchemaEntity139Create(
        entity_code="TEST_SPORTS_139",
        name="Test Entity 139",
        value_amount=139 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_139"
    assert obj.value_amount == 139 * 100.5

def test_sports_entity_140_schema_validation():
    obj = SportsSchemaEntity140Create(
        entity_code="TEST_SPORTS_140",
        name="Test Entity 140",
        value_amount=140 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_140"
    assert obj.value_amount == 140 * 100.5

def test_sports_entity_141_schema_validation():
    obj = SportsSchemaEntity141Create(
        entity_code="TEST_SPORTS_141",
        name="Test Entity 141",
        value_amount=141 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_141"
    assert obj.value_amount == 141 * 100.5

def test_sports_entity_142_schema_validation():
    obj = SportsSchemaEntity142Create(
        entity_code="TEST_SPORTS_142",
        name="Test Entity 142",
        value_amount=142 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_142"
    assert obj.value_amount == 142 * 100.5

def test_sports_entity_143_schema_validation():
    obj = SportsSchemaEntity143Create(
        entity_code="TEST_SPORTS_143",
        name="Test Entity 143",
        value_amount=143 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_143"
    assert obj.value_amount == 143 * 100.5

def test_sports_entity_144_schema_validation():
    obj = SportsSchemaEntity144Create(
        entity_code="TEST_SPORTS_144",
        name="Test Entity 144",
        value_amount=144 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_144"
    assert obj.value_amount == 144 * 100.5

def test_sports_entity_145_schema_validation():
    obj = SportsSchemaEntity145Create(
        entity_code="TEST_SPORTS_145",
        name="Test Entity 145",
        value_amount=145 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_145"
    assert obj.value_amount == 145 * 100.5

def test_sports_entity_146_schema_validation():
    obj = SportsSchemaEntity146Create(
        entity_code="TEST_SPORTS_146",
        name="Test Entity 146",
        value_amount=146 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_146"
    assert obj.value_amount == 146 * 100.5

def test_sports_entity_147_schema_validation():
    obj = SportsSchemaEntity147Create(
        entity_code="TEST_SPORTS_147",
        name="Test Entity 147",
        value_amount=147 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_147"
    assert obj.value_amount == 147 * 100.5

def test_sports_entity_148_schema_validation():
    obj = SportsSchemaEntity148Create(
        entity_code="TEST_SPORTS_148",
        name="Test Entity 148",
        value_amount=148 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_148"
    assert obj.value_amount == 148 * 100.5

def test_sports_entity_149_schema_validation():
    obj = SportsSchemaEntity149Create(
        entity_code="TEST_SPORTS_149",
        name="Test Entity 149",
        value_amount=149 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_149"
    assert obj.value_amount == 149 * 100.5

def test_sports_entity_150_schema_validation():
    obj = SportsSchemaEntity150Create(
        entity_code="TEST_SPORTS_150",
        name="Test Entity 150",
        value_amount=150 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_150"
    assert obj.value_amount == 150 * 100.5

def test_sports_entity_151_schema_validation():
    obj = SportsSchemaEntity151Create(
        entity_code="TEST_SPORTS_151",
        name="Test Entity 151",
        value_amount=151 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_151"
    assert obj.value_amount == 151 * 100.5

def test_sports_entity_152_schema_validation():
    obj = SportsSchemaEntity152Create(
        entity_code="TEST_SPORTS_152",
        name="Test Entity 152",
        value_amount=152 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_152"
    assert obj.value_amount == 152 * 100.5

def test_sports_entity_153_schema_validation():
    obj = SportsSchemaEntity153Create(
        entity_code="TEST_SPORTS_153",
        name="Test Entity 153",
        value_amount=153 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_153"
    assert obj.value_amount == 153 * 100.5

def test_sports_entity_154_schema_validation():
    obj = SportsSchemaEntity154Create(
        entity_code="TEST_SPORTS_154",
        name="Test Entity 154",
        value_amount=154 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_154"
    assert obj.value_amount == 154 * 100.5

def test_sports_entity_155_schema_validation():
    obj = SportsSchemaEntity155Create(
        entity_code="TEST_SPORTS_155",
        name="Test Entity 155",
        value_amount=155 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_155"
    assert obj.value_amount == 155 * 100.5

def test_sports_entity_156_schema_validation():
    obj = SportsSchemaEntity156Create(
        entity_code="TEST_SPORTS_156",
        name="Test Entity 156",
        value_amount=156 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_156"
    assert obj.value_amount == 156 * 100.5

def test_sports_entity_157_schema_validation():
    obj = SportsSchemaEntity157Create(
        entity_code="TEST_SPORTS_157",
        name="Test Entity 157",
        value_amount=157 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_157"
    assert obj.value_amount == 157 * 100.5

def test_sports_entity_158_schema_validation():
    obj = SportsSchemaEntity158Create(
        entity_code="TEST_SPORTS_158",
        name="Test Entity 158",
        value_amount=158 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_158"
    assert obj.value_amount == 158 * 100.5

def test_sports_entity_159_schema_validation():
    obj = SportsSchemaEntity159Create(
        entity_code="TEST_SPORTS_159",
        name="Test Entity 159",
        value_amount=159 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_159"
    assert obj.value_amount == 159 * 100.5

def test_sports_entity_160_schema_validation():
    obj = SportsSchemaEntity160Create(
        entity_code="TEST_SPORTS_160",
        name="Test Entity 160",
        value_amount=160 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_160"
    assert obj.value_amount == 160 * 100.5

def test_sports_entity_161_schema_validation():
    obj = SportsSchemaEntity161Create(
        entity_code="TEST_SPORTS_161",
        name="Test Entity 161",
        value_amount=161 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_161"
    assert obj.value_amount == 161 * 100.5

def test_sports_entity_162_schema_validation():
    obj = SportsSchemaEntity162Create(
        entity_code="TEST_SPORTS_162",
        name="Test Entity 162",
        value_amount=162 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_162"
    assert obj.value_amount == 162 * 100.5

def test_sports_entity_163_schema_validation():
    obj = SportsSchemaEntity163Create(
        entity_code="TEST_SPORTS_163",
        name="Test Entity 163",
        value_amount=163 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_163"
    assert obj.value_amount == 163 * 100.5

def test_sports_entity_164_schema_validation():
    obj = SportsSchemaEntity164Create(
        entity_code="TEST_SPORTS_164",
        name="Test Entity 164",
        value_amount=164 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_164"
    assert obj.value_amount == 164 * 100.5

def test_sports_entity_165_schema_validation():
    obj = SportsSchemaEntity165Create(
        entity_code="TEST_SPORTS_165",
        name="Test Entity 165",
        value_amount=165 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_165"
    assert obj.value_amount == 165 * 100.5

def test_sports_entity_166_schema_validation():
    obj = SportsSchemaEntity166Create(
        entity_code="TEST_SPORTS_166",
        name="Test Entity 166",
        value_amount=166 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_166"
    assert obj.value_amount == 166 * 100.5

def test_sports_entity_167_schema_validation():
    obj = SportsSchemaEntity167Create(
        entity_code="TEST_SPORTS_167",
        name="Test Entity 167",
        value_amount=167 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_167"
    assert obj.value_amount == 167 * 100.5

def test_sports_entity_168_schema_validation():
    obj = SportsSchemaEntity168Create(
        entity_code="TEST_SPORTS_168",
        name="Test Entity 168",
        value_amount=168 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_168"
    assert obj.value_amount == 168 * 100.5

def test_sports_entity_169_schema_validation():
    obj = SportsSchemaEntity169Create(
        entity_code="TEST_SPORTS_169",
        name="Test Entity 169",
        value_amount=169 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_169"
    assert obj.value_amount == 169 * 100.5

def test_sports_entity_170_schema_validation():
    obj = SportsSchemaEntity170Create(
        entity_code="TEST_SPORTS_170",
        name="Test Entity 170",
        value_amount=170 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_170"
    assert obj.value_amount == 170 * 100.5

def test_sports_entity_171_schema_validation():
    obj = SportsSchemaEntity171Create(
        entity_code="TEST_SPORTS_171",
        name="Test Entity 171",
        value_amount=171 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_171"
    assert obj.value_amount == 171 * 100.5

def test_sports_entity_172_schema_validation():
    obj = SportsSchemaEntity172Create(
        entity_code="TEST_SPORTS_172",
        name="Test Entity 172",
        value_amount=172 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_172"
    assert obj.value_amount == 172 * 100.5

def test_sports_entity_173_schema_validation():
    obj = SportsSchemaEntity173Create(
        entity_code="TEST_SPORTS_173",
        name="Test Entity 173",
        value_amount=173 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_173"
    assert obj.value_amount == 173 * 100.5

def test_sports_entity_174_schema_validation():
    obj = SportsSchemaEntity174Create(
        entity_code="TEST_SPORTS_174",
        name="Test Entity 174",
        value_amount=174 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_174"
    assert obj.value_amount == 174 * 100.5

def test_sports_entity_175_schema_validation():
    obj = SportsSchemaEntity175Create(
        entity_code="TEST_SPORTS_175",
        name="Test Entity 175",
        value_amount=175 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_175"
    assert obj.value_amount == 175 * 100.5

def test_sports_entity_176_schema_validation():
    obj = SportsSchemaEntity176Create(
        entity_code="TEST_SPORTS_176",
        name="Test Entity 176",
        value_amount=176 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_176"
    assert obj.value_amount == 176 * 100.5

def test_sports_entity_177_schema_validation():
    obj = SportsSchemaEntity177Create(
        entity_code="TEST_SPORTS_177",
        name="Test Entity 177",
        value_amount=177 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_177"
    assert obj.value_amount == 177 * 100.5

def test_sports_entity_178_schema_validation():
    obj = SportsSchemaEntity178Create(
        entity_code="TEST_SPORTS_178",
        name="Test Entity 178",
        value_amount=178 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_178"
    assert obj.value_amount == 178 * 100.5

def test_sports_entity_179_schema_validation():
    obj = SportsSchemaEntity179Create(
        entity_code="TEST_SPORTS_179",
        name="Test Entity 179",
        value_amount=179 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_179"
    assert obj.value_amount == 179 * 100.5

def test_sports_entity_180_schema_validation():
    obj = SportsSchemaEntity180Create(
        entity_code="TEST_SPORTS_180",
        name="Test Entity 180",
        value_amount=180 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_180"
    assert obj.value_amount == 180 * 100.5

def test_sports_entity_181_schema_validation():
    obj = SportsSchemaEntity181Create(
        entity_code="TEST_SPORTS_181",
        name="Test Entity 181",
        value_amount=181 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_181"
    assert obj.value_amount == 181 * 100.5

def test_sports_entity_182_schema_validation():
    obj = SportsSchemaEntity182Create(
        entity_code="TEST_SPORTS_182",
        name="Test Entity 182",
        value_amount=182 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_182"
    assert obj.value_amount == 182 * 100.5

def test_sports_entity_183_schema_validation():
    obj = SportsSchemaEntity183Create(
        entity_code="TEST_SPORTS_183",
        name="Test Entity 183",
        value_amount=183 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_183"
    assert obj.value_amount == 183 * 100.5

def test_sports_entity_184_schema_validation():
    obj = SportsSchemaEntity184Create(
        entity_code="TEST_SPORTS_184",
        name="Test Entity 184",
        value_amount=184 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_184"
    assert obj.value_amount == 184 * 100.5

def test_sports_entity_185_schema_validation():
    obj = SportsSchemaEntity185Create(
        entity_code="TEST_SPORTS_185",
        name="Test Entity 185",
        value_amount=185 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_185"
    assert obj.value_amount == 185 * 100.5

def test_sports_entity_186_schema_validation():
    obj = SportsSchemaEntity186Create(
        entity_code="TEST_SPORTS_186",
        name="Test Entity 186",
        value_amount=186 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_186"
    assert obj.value_amount == 186 * 100.5

def test_sports_entity_187_schema_validation():
    obj = SportsSchemaEntity187Create(
        entity_code="TEST_SPORTS_187",
        name="Test Entity 187",
        value_amount=187 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_187"
    assert obj.value_amount == 187 * 100.5

def test_sports_entity_188_schema_validation():
    obj = SportsSchemaEntity188Create(
        entity_code="TEST_SPORTS_188",
        name="Test Entity 188",
        value_amount=188 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_188"
    assert obj.value_amount == 188 * 100.5

def test_sports_entity_189_schema_validation():
    obj = SportsSchemaEntity189Create(
        entity_code="TEST_SPORTS_189",
        name="Test Entity 189",
        value_amount=189 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_189"
    assert obj.value_amount == 189 * 100.5

def test_sports_entity_190_schema_validation():
    obj = SportsSchemaEntity190Create(
        entity_code="TEST_SPORTS_190",
        name="Test Entity 190",
        value_amount=190 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_190"
    assert obj.value_amount == 190 * 100.5

def test_sports_entity_191_schema_validation():
    obj = SportsSchemaEntity191Create(
        entity_code="TEST_SPORTS_191",
        name="Test Entity 191",
        value_amount=191 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_191"
    assert obj.value_amount == 191 * 100.5

def test_sports_entity_192_schema_validation():
    obj = SportsSchemaEntity192Create(
        entity_code="TEST_SPORTS_192",
        name="Test Entity 192",
        value_amount=192 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_192"
    assert obj.value_amount == 192 * 100.5

def test_sports_entity_193_schema_validation():
    obj = SportsSchemaEntity193Create(
        entity_code="TEST_SPORTS_193",
        name="Test Entity 193",
        value_amount=193 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_193"
    assert obj.value_amount == 193 * 100.5

def test_sports_entity_194_schema_validation():
    obj = SportsSchemaEntity194Create(
        entity_code="TEST_SPORTS_194",
        name="Test Entity 194",
        value_amount=194 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_194"
    assert obj.value_amount == 194 * 100.5

def test_sports_entity_195_schema_validation():
    obj = SportsSchemaEntity195Create(
        entity_code="TEST_SPORTS_195",
        name="Test Entity 195",
        value_amount=195 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_195"
    assert obj.value_amount == 195 * 100.5

def test_sports_entity_196_schema_validation():
    obj = SportsSchemaEntity196Create(
        entity_code="TEST_SPORTS_196",
        name="Test Entity 196",
        value_amount=196 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_196"
    assert obj.value_amount == 196 * 100.5

def test_sports_entity_197_schema_validation():
    obj = SportsSchemaEntity197Create(
        entity_code="TEST_SPORTS_197",
        name="Test Entity 197",
        value_amount=197 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_197"
    assert obj.value_amount == 197 * 100.5

def test_sports_entity_198_schema_validation():
    obj = SportsSchemaEntity198Create(
        entity_code="TEST_SPORTS_198",
        name="Test Entity 198",
        value_amount=198 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_198"
    assert obj.value_amount == 198 * 100.5

def test_sports_entity_199_schema_validation():
    obj = SportsSchemaEntity199Create(
        entity_code="TEST_SPORTS_199",
        name="Test Entity 199",
        value_amount=199 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_199"
    assert obj.value_amount == 199 * 100.5

def test_sports_entity_200_schema_validation():
    obj = SportsSchemaEntity200Create(
        entity_code="TEST_SPORTS_200",
        name="Test Entity 200",
        value_amount=200 * 100.5
    )
    assert obj.entity_code == "TEST_SPORTS_200"
    assert obj.value_amount == 200 * 100.5


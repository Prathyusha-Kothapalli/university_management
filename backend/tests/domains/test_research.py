"""
Pytest suite for Research, Grants & Lab Inventory
"""
import pytest
from app.domains.research.schemas import *

def test_research_entity_1_schema_validation():
    obj = ResearchSchemaEntity1Create(
        entity_code="TEST_RESEARCH_1",
        name="Test Entity 1",
        value_amount=1 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_1"
    assert obj.value_amount == 1 * 100.5

def test_research_entity_2_schema_validation():
    obj = ResearchSchemaEntity2Create(
        entity_code="TEST_RESEARCH_2",
        name="Test Entity 2",
        value_amount=2 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_2"
    assert obj.value_amount == 2 * 100.5

def test_research_entity_3_schema_validation():
    obj = ResearchSchemaEntity3Create(
        entity_code="TEST_RESEARCH_3",
        name="Test Entity 3",
        value_amount=3 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_3"
    assert obj.value_amount == 3 * 100.5

def test_research_entity_4_schema_validation():
    obj = ResearchSchemaEntity4Create(
        entity_code="TEST_RESEARCH_4",
        name="Test Entity 4",
        value_amount=4 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_4"
    assert obj.value_amount == 4 * 100.5

def test_research_entity_5_schema_validation():
    obj = ResearchSchemaEntity5Create(
        entity_code="TEST_RESEARCH_5",
        name="Test Entity 5",
        value_amount=5 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_5"
    assert obj.value_amount == 5 * 100.5

def test_research_entity_6_schema_validation():
    obj = ResearchSchemaEntity6Create(
        entity_code="TEST_RESEARCH_6",
        name="Test Entity 6",
        value_amount=6 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_6"
    assert obj.value_amount == 6 * 100.5

def test_research_entity_7_schema_validation():
    obj = ResearchSchemaEntity7Create(
        entity_code="TEST_RESEARCH_7",
        name="Test Entity 7",
        value_amount=7 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_7"
    assert obj.value_amount == 7 * 100.5

def test_research_entity_8_schema_validation():
    obj = ResearchSchemaEntity8Create(
        entity_code="TEST_RESEARCH_8",
        name="Test Entity 8",
        value_amount=8 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_8"
    assert obj.value_amount == 8 * 100.5

def test_research_entity_9_schema_validation():
    obj = ResearchSchemaEntity9Create(
        entity_code="TEST_RESEARCH_9",
        name="Test Entity 9",
        value_amount=9 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_9"
    assert obj.value_amount == 9 * 100.5

def test_research_entity_10_schema_validation():
    obj = ResearchSchemaEntity10Create(
        entity_code="TEST_RESEARCH_10",
        name="Test Entity 10",
        value_amount=10 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_10"
    assert obj.value_amount == 10 * 100.5

def test_research_entity_11_schema_validation():
    obj = ResearchSchemaEntity11Create(
        entity_code="TEST_RESEARCH_11",
        name="Test Entity 11",
        value_amount=11 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_11"
    assert obj.value_amount == 11 * 100.5

def test_research_entity_12_schema_validation():
    obj = ResearchSchemaEntity12Create(
        entity_code="TEST_RESEARCH_12",
        name="Test Entity 12",
        value_amount=12 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_12"
    assert obj.value_amount == 12 * 100.5

def test_research_entity_13_schema_validation():
    obj = ResearchSchemaEntity13Create(
        entity_code="TEST_RESEARCH_13",
        name="Test Entity 13",
        value_amount=13 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_13"
    assert obj.value_amount == 13 * 100.5

def test_research_entity_14_schema_validation():
    obj = ResearchSchemaEntity14Create(
        entity_code="TEST_RESEARCH_14",
        name="Test Entity 14",
        value_amount=14 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_14"
    assert obj.value_amount == 14 * 100.5

def test_research_entity_15_schema_validation():
    obj = ResearchSchemaEntity15Create(
        entity_code="TEST_RESEARCH_15",
        name="Test Entity 15",
        value_amount=15 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_15"
    assert obj.value_amount == 15 * 100.5

def test_research_entity_16_schema_validation():
    obj = ResearchSchemaEntity16Create(
        entity_code="TEST_RESEARCH_16",
        name="Test Entity 16",
        value_amount=16 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_16"
    assert obj.value_amount == 16 * 100.5

def test_research_entity_17_schema_validation():
    obj = ResearchSchemaEntity17Create(
        entity_code="TEST_RESEARCH_17",
        name="Test Entity 17",
        value_amount=17 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_17"
    assert obj.value_amount == 17 * 100.5

def test_research_entity_18_schema_validation():
    obj = ResearchSchemaEntity18Create(
        entity_code="TEST_RESEARCH_18",
        name="Test Entity 18",
        value_amount=18 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_18"
    assert obj.value_amount == 18 * 100.5

def test_research_entity_19_schema_validation():
    obj = ResearchSchemaEntity19Create(
        entity_code="TEST_RESEARCH_19",
        name="Test Entity 19",
        value_amount=19 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_19"
    assert obj.value_amount == 19 * 100.5

def test_research_entity_20_schema_validation():
    obj = ResearchSchemaEntity20Create(
        entity_code="TEST_RESEARCH_20",
        name="Test Entity 20",
        value_amount=20 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_20"
    assert obj.value_amount == 20 * 100.5

def test_research_entity_21_schema_validation():
    obj = ResearchSchemaEntity21Create(
        entity_code="TEST_RESEARCH_21",
        name="Test Entity 21",
        value_amount=21 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_21"
    assert obj.value_amount == 21 * 100.5

def test_research_entity_22_schema_validation():
    obj = ResearchSchemaEntity22Create(
        entity_code="TEST_RESEARCH_22",
        name="Test Entity 22",
        value_amount=22 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_22"
    assert obj.value_amount == 22 * 100.5

def test_research_entity_23_schema_validation():
    obj = ResearchSchemaEntity23Create(
        entity_code="TEST_RESEARCH_23",
        name="Test Entity 23",
        value_amount=23 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_23"
    assert obj.value_amount == 23 * 100.5

def test_research_entity_24_schema_validation():
    obj = ResearchSchemaEntity24Create(
        entity_code="TEST_RESEARCH_24",
        name="Test Entity 24",
        value_amount=24 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_24"
    assert obj.value_amount == 24 * 100.5

def test_research_entity_25_schema_validation():
    obj = ResearchSchemaEntity25Create(
        entity_code="TEST_RESEARCH_25",
        name="Test Entity 25",
        value_amount=25 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_25"
    assert obj.value_amount == 25 * 100.5

def test_research_entity_26_schema_validation():
    obj = ResearchSchemaEntity26Create(
        entity_code="TEST_RESEARCH_26",
        name="Test Entity 26",
        value_amount=26 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_26"
    assert obj.value_amount == 26 * 100.5

def test_research_entity_27_schema_validation():
    obj = ResearchSchemaEntity27Create(
        entity_code="TEST_RESEARCH_27",
        name="Test Entity 27",
        value_amount=27 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_27"
    assert obj.value_amount == 27 * 100.5

def test_research_entity_28_schema_validation():
    obj = ResearchSchemaEntity28Create(
        entity_code="TEST_RESEARCH_28",
        name="Test Entity 28",
        value_amount=28 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_28"
    assert obj.value_amount == 28 * 100.5

def test_research_entity_29_schema_validation():
    obj = ResearchSchemaEntity29Create(
        entity_code="TEST_RESEARCH_29",
        name="Test Entity 29",
        value_amount=29 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_29"
    assert obj.value_amount == 29 * 100.5

def test_research_entity_30_schema_validation():
    obj = ResearchSchemaEntity30Create(
        entity_code="TEST_RESEARCH_30",
        name="Test Entity 30",
        value_amount=30 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_30"
    assert obj.value_amount == 30 * 100.5

def test_research_entity_31_schema_validation():
    obj = ResearchSchemaEntity31Create(
        entity_code="TEST_RESEARCH_31",
        name="Test Entity 31",
        value_amount=31 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_31"
    assert obj.value_amount == 31 * 100.5

def test_research_entity_32_schema_validation():
    obj = ResearchSchemaEntity32Create(
        entity_code="TEST_RESEARCH_32",
        name="Test Entity 32",
        value_amount=32 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_32"
    assert obj.value_amount == 32 * 100.5

def test_research_entity_33_schema_validation():
    obj = ResearchSchemaEntity33Create(
        entity_code="TEST_RESEARCH_33",
        name="Test Entity 33",
        value_amount=33 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_33"
    assert obj.value_amount == 33 * 100.5

def test_research_entity_34_schema_validation():
    obj = ResearchSchemaEntity34Create(
        entity_code="TEST_RESEARCH_34",
        name="Test Entity 34",
        value_amount=34 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_34"
    assert obj.value_amount == 34 * 100.5

def test_research_entity_35_schema_validation():
    obj = ResearchSchemaEntity35Create(
        entity_code="TEST_RESEARCH_35",
        name="Test Entity 35",
        value_amount=35 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_35"
    assert obj.value_amount == 35 * 100.5

def test_research_entity_36_schema_validation():
    obj = ResearchSchemaEntity36Create(
        entity_code="TEST_RESEARCH_36",
        name="Test Entity 36",
        value_amount=36 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_36"
    assert obj.value_amount == 36 * 100.5

def test_research_entity_37_schema_validation():
    obj = ResearchSchemaEntity37Create(
        entity_code="TEST_RESEARCH_37",
        name="Test Entity 37",
        value_amount=37 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_37"
    assert obj.value_amount == 37 * 100.5

def test_research_entity_38_schema_validation():
    obj = ResearchSchemaEntity38Create(
        entity_code="TEST_RESEARCH_38",
        name="Test Entity 38",
        value_amount=38 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_38"
    assert obj.value_amount == 38 * 100.5

def test_research_entity_39_schema_validation():
    obj = ResearchSchemaEntity39Create(
        entity_code="TEST_RESEARCH_39",
        name="Test Entity 39",
        value_amount=39 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_39"
    assert obj.value_amount == 39 * 100.5

def test_research_entity_40_schema_validation():
    obj = ResearchSchemaEntity40Create(
        entity_code="TEST_RESEARCH_40",
        name="Test Entity 40",
        value_amount=40 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_40"
    assert obj.value_amount == 40 * 100.5

def test_research_entity_41_schema_validation():
    obj = ResearchSchemaEntity41Create(
        entity_code="TEST_RESEARCH_41",
        name="Test Entity 41",
        value_amount=41 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_41"
    assert obj.value_amount == 41 * 100.5

def test_research_entity_42_schema_validation():
    obj = ResearchSchemaEntity42Create(
        entity_code="TEST_RESEARCH_42",
        name="Test Entity 42",
        value_amount=42 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_42"
    assert obj.value_amount == 42 * 100.5

def test_research_entity_43_schema_validation():
    obj = ResearchSchemaEntity43Create(
        entity_code="TEST_RESEARCH_43",
        name="Test Entity 43",
        value_amount=43 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_43"
    assert obj.value_amount == 43 * 100.5

def test_research_entity_44_schema_validation():
    obj = ResearchSchemaEntity44Create(
        entity_code="TEST_RESEARCH_44",
        name="Test Entity 44",
        value_amount=44 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_44"
    assert obj.value_amount == 44 * 100.5

def test_research_entity_45_schema_validation():
    obj = ResearchSchemaEntity45Create(
        entity_code="TEST_RESEARCH_45",
        name="Test Entity 45",
        value_amount=45 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_45"
    assert obj.value_amount == 45 * 100.5

def test_research_entity_46_schema_validation():
    obj = ResearchSchemaEntity46Create(
        entity_code="TEST_RESEARCH_46",
        name="Test Entity 46",
        value_amount=46 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_46"
    assert obj.value_amount == 46 * 100.5

def test_research_entity_47_schema_validation():
    obj = ResearchSchemaEntity47Create(
        entity_code="TEST_RESEARCH_47",
        name="Test Entity 47",
        value_amount=47 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_47"
    assert obj.value_amount == 47 * 100.5

def test_research_entity_48_schema_validation():
    obj = ResearchSchemaEntity48Create(
        entity_code="TEST_RESEARCH_48",
        name="Test Entity 48",
        value_amount=48 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_48"
    assert obj.value_amount == 48 * 100.5

def test_research_entity_49_schema_validation():
    obj = ResearchSchemaEntity49Create(
        entity_code="TEST_RESEARCH_49",
        name="Test Entity 49",
        value_amount=49 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_49"
    assert obj.value_amount == 49 * 100.5

def test_research_entity_50_schema_validation():
    obj = ResearchSchemaEntity50Create(
        entity_code="TEST_RESEARCH_50",
        name="Test Entity 50",
        value_amount=50 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_50"
    assert obj.value_amount == 50 * 100.5

def test_research_entity_51_schema_validation():
    obj = ResearchSchemaEntity51Create(
        entity_code="TEST_RESEARCH_51",
        name="Test Entity 51",
        value_amount=51 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_51"
    assert obj.value_amount == 51 * 100.5

def test_research_entity_52_schema_validation():
    obj = ResearchSchemaEntity52Create(
        entity_code="TEST_RESEARCH_52",
        name="Test Entity 52",
        value_amount=52 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_52"
    assert obj.value_amount == 52 * 100.5

def test_research_entity_53_schema_validation():
    obj = ResearchSchemaEntity53Create(
        entity_code="TEST_RESEARCH_53",
        name="Test Entity 53",
        value_amount=53 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_53"
    assert obj.value_amount == 53 * 100.5

def test_research_entity_54_schema_validation():
    obj = ResearchSchemaEntity54Create(
        entity_code="TEST_RESEARCH_54",
        name="Test Entity 54",
        value_amount=54 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_54"
    assert obj.value_amount == 54 * 100.5

def test_research_entity_55_schema_validation():
    obj = ResearchSchemaEntity55Create(
        entity_code="TEST_RESEARCH_55",
        name="Test Entity 55",
        value_amount=55 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_55"
    assert obj.value_amount == 55 * 100.5

def test_research_entity_56_schema_validation():
    obj = ResearchSchemaEntity56Create(
        entity_code="TEST_RESEARCH_56",
        name="Test Entity 56",
        value_amount=56 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_56"
    assert obj.value_amount == 56 * 100.5

def test_research_entity_57_schema_validation():
    obj = ResearchSchemaEntity57Create(
        entity_code="TEST_RESEARCH_57",
        name="Test Entity 57",
        value_amount=57 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_57"
    assert obj.value_amount == 57 * 100.5

def test_research_entity_58_schema_validation():
    obj = ResearchSchemaEntity58Create(
        entity_code="TEST_RESEARCH_58",
        name="Test Entity 58",
        value_amount=58 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_58"
    assert obj.value_amount == 58 * 100.5

def test_research_entity_59_schema_validation():
    obj = ResearchSchemaEntity59Create(
        entity_code="TEST_RESEARCH_59",
        name="Test Entity 59",
        value_amount=59 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_59"
    assert obj.value_amount == 59 * 100.5

def test_research_entity_60_schema_validation():
    obj = ResearchSchemaEntity60Create(
        entity_code="TEST_RESEARCH_60",
        name="Test Entity 60",
        value_amount=60 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_60"
    assert obj.value_amount == 60 * 100.5

def test_research_entity_61_schema_validation():
    obj = ResearchSchemaEntity61Create(
        entity_code="TEST_RESEARCH_61",
        name="Test Entity 61",
        value_amount=61 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_61"
    assert obj.value_amount == 61 * 100.5

def test_research_entity_62_schema_validation():
    obj = ResearchSchemaEntity62Create(
        entity_code="TEST_RESEARCH_62",
        name="Test Entity 62",
        value_amount=62 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_62"
    assert obj.value_amount == 62 * 100.5

def test_research_entity_63_schema_validation():
    obj = ResearchSchemaEntity63Create(
        entity_code="TEST_RESEARCH_63",
        name="Test Entity 63",
        value_amount=63 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_63"
    assert obj.value_amount == 63 * 100.5

def test_research_entity_64_schema_validation():
    obj = ResearchSchemaEntity64Create(
        entity_code="TEST_RESEARCH_64",
        name="Test Entity 64",
        value_amount=64 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_64"
    assert obj.value_amount == 64 * 100.5

def test_research_entity_65_schema_validation():
    obj = ResearchSchemaEntity65Create(
        entity_code="TEST_RESEARCH_65",
        name="Test Entity 65",
        value_amount=65 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_65"
    assert obj.value_amount == 65 * 100.5

def test_research_entity_66_schema_validation():
    obj = ResearchSchemaEntity66Create(
        entity_code="TEST_RESEARCH_66",
        name="Test Entity 66",
        value_amount=66 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_66"
    assert obj.value_amount == 66 * 100.5

def test_research_entity_67_schema_validation():
    obj = ResearchSchemaEntity67Create(
        entity_code="TEST_RESEARCH_67",
        name="Test Entity 67",
        value_amount=67 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_67"
    assert obj.value_amount == 67 * 100.5

def test_research_entity_68_schema_validation():
    obj = ResearchSchemaEntity68Create(
        entity_code="TEST_RESEARCH_68",
        name="Test Entity 68",
        value_amount=68 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_68"
    assert obj.value_amount == 68 * 100.5

def test_research_entity_69_schema_validation():
    obj = ResearchSchemaEntity69Create(
        entity_code="TEST_RESEARCH_69",
        name="Test Entity 69",
        value_amount=69 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_69"
    assert obj.value_amount == 69 * 100.5

def test_research_entity_70_schema_validation():
    obj = ResearchSchemaEntity70Create(
        entity_code="TEST_RESEARCH_70",
        name="Test Entity 70",
        value_amount=70 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_70"
    assert obj.value_amount == 70 * 100.5

def test_research_entity_71_schema_validation():
    obj = ResearchSchemaEntity71Create(
        entity_code="TEST_RESEARCH_71",
        name="Test Entity 71",
        value_amount=71 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_71"
    assert obj.value_amount == 71 * 100.5

def test_research_entity_72_schema_validation():
    obj = ResearchSchemaEntity72Create(
        entity_code="TEST_RESEARCH_72",
        name="Test Entity 72",
        value_amount=72 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_72"
    assert obj.value_amount == 72 * 100.5

def test_research_entity_73_schema_validation():
    obj = ResearchSchemaEntity73Create(
        entity_code="TEST_RESEARCH_73",
        name="Test Entity 73",
        value_amount=73 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_73"
    assert obj.value_amount == 73 * 100.5

def test_research_entity_74_schema_validation():
    obj = ResearchSchemaEntity74Create(
        entity_code="TEST_RESEARCH_74",
        name="Test Entity 74",
        value_amount=74 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_74"
    assert obj.value_amount == 74 * 100.5

def test_research_entity_75_schema_validation():
    obj = ResearchSchemaEntity75Create(
        entity_code="TEST_RESEARCH_75",
        name="Test Entity 75",
        value_amount=75 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_75"
    assert obj.value_amount == 75 * 100.5

def test_research_entity_76_schema_validation():
    obj = ResearchSchemaEntity76Create(
        entity_code="TEST_RESEARCH_76",
        name="Test Entity 76",
        value_amount=76 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_76"
    assert obj.value_amount == 76 * 100.5

def test_research_entity_77_schema_validation():
    obj = ResearchSchemaEntity77Create(
        entity_code="TEST_RESEARCH_77",
        name="Test Entity 77",
        value_amount=77 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_77"
    assert obj.value_amount == 77 * 100.5

def test_research_entity_78_schema_validation():
    obj = ResearchSchemaEntity78Create(
        entity_code="TEST_RESEARCH_78",
        name="Test Entity 78",
        value_amount=78 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_78"
    assert obj.value_amount == 78 * 100.5

def test_research_entity_79_schema_validation():
    obj = ResearchSchemaEntity79Create(
        entity_code="TEST_RESEARCH_79",
        name="Test Entity 79",
        value_amount=79 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_79"
    assert obj.value_amount == 79 * 100.5

def test_research_entity_80_schema_validation():
    obj = ResearchSchemaEntity80Create(
        entity_code="TEST_RESEARCH_80",
        name="Test Entity 80",
        value_amount=80 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_80"
    assert obj.value_amount == 80 * 100.5

def test_research_entity_81_schema_validation():
    obj = ResearchSchemaEntity81Create(
        entity_code="TEST_RESEARCH_81",
        name="Test Entity 81",
        value_amount=81 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_81"
    assert obj.value_amount == 81 * 100.5

def test_research_entity_82_schema_validation():
    obj = ResearchSchemaEntity82Create(
        entity_code="TEST_RESEARCH_82",
        name="Test Entity 82",
        value_amount=82 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_82"
    assert obj.value_amount == 82 * 100.5

def test_research_entity_83_schema_validation():
    obj = ResearchSchemaEntity83Create(
        entity_code="TEST_RESEARCH_83",
        name="Test Entity 83",
        value_amount=83 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_83"
    assert obj.value_amount == 83 * 100.5

def test_research_entity_84_schema_validation():
    obj = ResearchSchemaEntity84Create(
        entity_code="TEST_RESEARCH_84",
        name="Test Entity 84",
        value_amount=84 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_84"
    assert obj.value_amount == 84 * 100.5

def test_research_entity_85_schema_validation():
    obj = ResearchSchemaEntity85Create(
        entity_code="TEST_RESEARCH_85",
        name="Test Entity 85",
        value_amount=85 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_85"
    assert obj.value_amount == 85 * 100.5

def test_research_entity_86_schema_validation():
    obj = ResearchSchemaEntity86Create(
        entity_code="TEST_RESEARCH_86",
        name="Test Entity 86",
        value_amount=86 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_86"
    assert obj.value_amount == 86 * 100.5

def test_research_entity_87_schema_validation():
    obj = ResearchSchemaEntity87Create(
        entity_code="TEST_RESEARCH_87",
        name="Test Entity 87",
        value_amount=87 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_87"
    assert obj.value_amount == 87 * 100.5

def test_research_entity_88_schema_validation():
    obj = ResearchSchemaEntity88Create(
        entity_code="TEST_RESEARCH_88",
        name="Test Entity 88",
        value_amount=88 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_88"
    assert obj.value_amount == 88 * 100.5

def test_research_entity_89_schema_validation():
    obj = ResearchSchemaEntity89Create(
        entity_code="TEST_RESEARCH_89",
        name="Test Entity 89",
        value_amount=89 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_89"
    assert obj.value_amount == 89 * 100.5

def test_research_entity_90_schema_validation():
    obj = ResearchSchemaEntity90Create(
        entity_code="TEST_RESEARCH_90",
        name="Test Entity 90",
        value_amount=90 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_90"
    assert obj.value_amount == 90 * 100.5

def test_research_entity_91_schema_validation():
    obj = ResearchSchemaEntity91Create(
        entity_code="TEST_RESEARCH_91",
        name="Test Entity 91",
        value_amount=91 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_91"
    assert obj.value_amount == 91 * 100.5

def test_research_entity_92_schema_validation():
    obj = ResearchSchemaEntity92Create(
        entity_code="TEST_RESEARCH_92",
        name="Test Entity 92",
        value_amount=92 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_92"
    assert obj.value_amount == 92 * 100.5

def test_research_entity_93_schema_validation():
    obj = ResearchSchemaEntity93Create(
        entity_code="TEST_RESEARCH_93",
        name="Test Entity 93",
        value_amount=93 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_93"
    assert obj.value_amount == 93 * 100.5

def test_research_entity_94_schema_validation():
    obj = ResearchSchemaEntity94Create(
        entity_code="TEST_RESEARCH_94",
        name="Test Entity 94",
        value_amount=94 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_94"
    assert obj.value_amount == 94 * 100.5

def test_research_entity_95_schema_validation():
    obj = ResearchSchemaEntity95Create(
        entity_code="TEST_RESEARCH_95",
        name="Test Entity 95",
        value_amount=95 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_95"
    assert obj.value_amount == 95 * 100.5

def test_research_entity_96_schema_validation():
    obj = ResearchSchemaEntity96Create(
        entity_code="TEST_RESEARCH_96",
        name="Test Entity 96",
        value_amount=96 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_96"
    assert obj.value_amount == 96 * 100.5

def test_research_entity_97_schema_validation():
    obj = ResearchSchemaEntity97Create(
        entity_code="TEST_RESEARCH_97",
        name="Test Entity 97",
        value_amount=97 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_97"
    assert obj.value_amount == 97 * 100.5

def test_research_entity_98_schema_validation():
    obj = ResearchSchemaEntity98Create(
        entity_code="TEST_RESEARCH_98",
        name="Test Entity 98",
        value_amount=98 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_98"
    assert obj.value_amount == 98 * 100.5

def test_research_entity_99_schema_validation():
    obj = ResearchSchemaEntity99Create(
        entity_code="TEST_RESEARCH_99",
        name="Test Entity 99",
        value_amount=99 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_99"
    assert obj.value_amount == 99 * 100.5

def test_research_entity_100_schema_validation():
    obj = ResearchSchemaEntity100Create(
        entity_code="TEST_RESEARCH_100",
        name="Test Entity 100",
        value_amount=100 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_100"
    assert obj.value_amount == 100 * 100.5

def test_research_entity_101_schema_validation():
    obj = ResearchSchemaEntity101Create(
        entity_code="TEST_RESEARCH_101",
        name="Test Entity 101",
        value_amount=101 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_101"
    assert obj.value_amount == 101 * 100.5

def test_research_entity_102_schema_validation():
    obj = ResearchSchemaEntity102Create(
        entity_code="TEST_RESEARCH_102",
        name="Test Entity 102",
        value_amount=102 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_102"
    assert obj.value_amount == 102 * 100.5

def test_research_entity_103_schema_validation():
    obj = ResearchSchemaEntity103Create(
        entity_code="TEST_RESEARCH_103",
        name="Test Entity 103",
        value_amount=103 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_103"
    assert obj.value_amount == 103 * 100.5

def test_research_entity_104_schema_validation():
    obj = ResearchSchemaEntity104Create(
        entity_code="TEST_RESEARCH_104",
        name="Test Entity 104",
        value_amount=104 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_104"
    assert obj.value_amount == 104 * 100.5

def test_research_entity_105_schema_validation():
    obj = ResearchSchemaEntity105Create(
        entity_code="TEST_RESEARCH_105",
        name="Test Entity 105",
        value_amount=105 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_105"
    assert obj.value_amount == 105 * 100.5

def test_research_entity_106_schema_validation():
    obj = ResearchSchemaEntity106Create(
        entity_code="TEST_RESEARCH_106",
        name="Test Entity 106",
        value_amount=106 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_106"
    assert obj.value_amount == 106 * 100.5

def test_research_entity_107_schema_validation():
    obj = ResearchSchemaEntity107Create(
        entity_code="TEST_RESEARCH_107",
        name="Test Entity 107",
        value_amount=107 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_107"
    assert obj.value_amount == 107 * 100.5

def test_research_entity_108_schema_validation():
    obj = ResearchSchemaEntity108Create(
        entity_code="TEST_RESEARCH_108",
        name="Test Entity 108",
        value_amount=108 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_108"
    assert obj.value_amount == 108 * 100.5

def test_research_entity_109_schema_validation():
    obj = ResearchSchemaEntity109Create(
        entity_code="TEST_RESEARCH_109",
        name="Test Entity 109",
        value_amount=109 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_109"
    assert obj.value_amount == 109 * 100.5

def test_research_entity_110_schema_validation():
    obj = ResearchSchemaEntity110Create(
        entity_code="TEST_RESEARCH_110",
        name="Test Entity 110",
        value_amount=110 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_110"
    assert obj.value_amount == 110 * 100.5

def test_research_entity_111_schema_validation():
    obj = ResearchSchemaEntity111Create(
        entity_code="TEST_RESEARCH_111",
        name="Test Entity 111",
        value_amount=111 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_111"
    assert obj.value_amount == 111 * 100.5

def test_research_entity_112_schema_validation():
    obj = ResearchSchemaEntity112Create(
        entity_code="TEST_RESEARCH_112",
        name="Test Entity 112",
        value_amount=112 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_112"
    assert obj.value_amount == 112 * 100.5

def test_research_entity_113_schema_validation():
    obj = ResearchSchemaEntity113Create(
        entity_code="TEST_RESEARCH_113",
        name="Test Entity 113",
        value_amount=113 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_113"
    assert obj.value_amount == 113 * 100.5

def test_research_entity_114_schema_validation():
    obj = ResearchSchemaEntity114Create(
        entity_code="TEST_RESEARCH_114",
        name="Test Entity 114",
        value_amount=114 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_114"
    assert obj.value_amount == 114 * 100.5

def test_research_entity_115_schema_validation():
    obj = ResearchSchemaEntity115Create(
        entity_code="TEST_RESEARCH_115",
        name="Test Entity 115",
        value_amount=115 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_115"
    assert obj.value_amount == 115 * 100.5

def test_research_entity_116_schema_validation():
    obj = ResearchSchemaEntity116Create(
        entity_code="TEST_RESEARCH_116",
        name="Test Entity 116",
        value_amount=116 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_116"
    assert obj.value_amount == 116 * 100.5

def test_research_entity_117_schema_validation():
    obj = ResearchSchemaEntity117Create(
        entity_code="TEST_RESEARCH_117",
        name="Test Entity 117",
        value_amount=117 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_117"
    assert obj.value_amount == 117 * 100.5

def test_research_entity_118_schema_validation():
    obj = ResearchSchemaEntity118Create(
        entity_code="TEST_RESEARCH_118",
        name="Test Entity 118",
        value_amount=118 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_118"
    assert obj.value_amount == 118 * 100.5

def test_research_entity_119_schema_validation():
    obj = ResearchSchemaEntity119Create(
        entity_code="TEST_RESEARCH_119",
        name="Test Entity 119",
        value_amount=119 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_119"
    assert obj.value_amount == 119 * 100.5

def test_research_entity_120_schema_validation():
    obj = ResearchSchemaEntity120Create(
        entity_code="TEST_RESEARCH_120",
        name="Test Entity 120",
        value_amount=120 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_120"
    assert obj.value_amount == 120 * 100.5

def test_research_entity_121_schema_validation():
    obj = ResearchSchemaEntity121Create(
        entity_code="TEST_RESEARCH_121",
        name="Test Entity 121",
        value_amount=121 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_121"
    assert obj.value_amount == 121 * 100.5

def test_research_entity_122_schema_validation():
    obj = ResearchSchemaEntity122Create(
        entity_code="TEST_RESEARCH_122",
        name="Test Entity 122",
        value_amount=122 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_122"
    assert obj.value_amount == 122 * 100.5

def test_research_entity_123_schema_validation():
    obj = ResearchSchemaEntity123Create(
        entity_code="TEST_RESEARCH_123",
        name="Test Entity 123",
        value_amount=123 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_123"
    assert obj.value_amount == 123 * 100.5

def test_research_entity_124_schema_validation():
    obj = ResearchSchemaEntity124Create(
        entity_code="TEST_RESEARCH_124",
        name="Test Entity 124",
        value_amount=124 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_124"
    assert obj.value_amount == 124 * 100.5

def test_research_entity_125_schema_validation():
    obj = ResearchSchemaEntity125Create(
        entity_code="TEST_RESEARCH_125",
        name="Test Entity 125",
        value_amount=125 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_125"
    assert obj.value_amount == 125 * 100.5

def test_research_entity_126_schema_validation():
    obj = ResearchSchemaEntity126Create(
        entity_code="TEST_RESEARCH_126",
        name="Test Entity 126",
        value_amount=126 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_126"
    assert obj.value_amount == 126 * 100.5

def test_research_entity_127_schema_validation():
    obj = ResearchSchemaEntity127Create(
        entity_code="TEST_RESEARCH_127",
        name="Test Entity 127",
        value_amount=127 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_127"
    assert obj.value_amount == 127 * 100.5

def test_research_entity_128_schema_validation():
    obj = ResearchSchemaEntity128Create(
        entity_code="TEST_RESEARCH_128",
        name="Test Entity 128",
        value_amount=128 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_128"
    assert obj.value_amount == 128 * 100.5

def test_research_entity_129_schema_validation():
    obj = ResearchSchemaEntity129Create(
        entity_code="TEST_RESEARCH_129",
        name="Test Entity 129",
        value_amount=129 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_129"
    assert obj.value_amount == 129 * 100.5

def test_research_entity_130_schema_validation():
    obj = ResearchSchemaEntity130Create(
        entity_code="TEST_RESEARCH_130",
        name="Test Entity 130",
        value_amount=130 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_130"
    assert obj.value_amount == 130 * 100.5

def test_research_entity_131_schema_validation():
    obj = ResearchSchemaEntity131Create(
        entity_code="TEST_RESEARCH_131",
        name="Test Entity 131",
        value_amount=131 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_131"
    assert obj.value_amount == 131 * 100.5

def test_research_entity_132_schema_validation():
    obj = ResearchSchemaEntity132Create(
        entity_code="TEST_RESEARCH_132",
        name="Test Entity 132",
        value_amount=132 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_132"
    assert obj.value_amount == 132 * 100.5

def test_research_entity_133_schema_validation():
    obj = ResearchSchemaEntity133Create(
        entity_code="TEST_RESEARCH_133",
        name="Test Entity 133",
        value_amount=133 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_133"
    assert obj.value_amount == 133 * 100.5

def test_research_entity_134_schema_validation():
    obj = ResearchSchemaEntity134Create(
        entity_code="TEST_RESEARCH_134",
        name="Test Entity 134",
        value_amount=134 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_134"
    assert obj.value_amount == 134 * 100.5

def test_research_entity_135_schema_validation():
    obj = ResearchSchemaEntity135Create(
        entity_code="TEST_RESEARCH_135",
        name="Test Entity 135",
        value_amount=135 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_135"
    assert obj.value_amount == 135 * 100.5

def test_research_entity_136_schema_validation():
    obj = ResearchSchemaEntity136Create(
        entity_code="TEST_RESEARCH_136",
        name="Test Entity 136",
        value_amount=136 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_136"
    assert obj.value_amount == 136 * 100.5

def test_research_entity_137_schema_validation():
    obj = ResearchSchemaEntity137Create(
        entity_code="TEST_RESEARCH_137",
        name="Test Entity 137",
        value_amount=137 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_137"
    assert obj.value_amount == 137 * 100.5

def test_research_entity_138_schema_validation():
    obj = ResearchSchemaEntity138Create(
        entity_code="TEST_RESEARCH_138",
        name="Test Entity 138",
        value_amount=138 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_138"
    assert obj.value_amount == 138 * 100.5

def test_research_entity_139_schema_validation():
    obj = ResearchSchemaEntity139Create(
        entity_code="TEST_RESEARCH_139",
        name="Test Entity 139",
        value_amount=139 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_139"
    assert obj.value_amount == 139 * 100.5

def test_research_entity_140_schema_validation():
    obj = ResearchSchemaEntity140Create(
        entity_code="TEST_RESEARCH_140",
        name="Test Entity 140",
        value_amount=140 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_140"
    assert obj.value_amount == 140 * 100.5

def test_research_entity_141_schema_validation():
    obj = ResearchSchemaEntity141Create(
        entity_code="TEST_RESEARCH_141",
        name="Test Entity 141",
        value_amount=141 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_141"
    assert obj.value_amount == 141 * 100.5

def test_research_entity_142_schema_validation():
    obj = ResearchSchemaEntity142Create(
        entity_code="TEST_RESEARCH_142",
        name="Test Entity 142",
        value_amount=142 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_142"
    assert obj.value_amount == 142 * 100.5

def test_research_entity_143_schema_validation():
    obj = ResearchSchemaEntity143Create(
        entity_code="TEST_RESEARCH_143",
        name="Test Entity 143",
        value_amount=143 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_143"
    assert obj.value_amount == 143 * 100.5

def test_research_entity_144_schema_validation():
    obj = ResearchSchemaEntity144Create(
        entity_code="TEST_RESEARCH_144",
        name="Test Entity 144",
        value_amount=144 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_144"
    assert obj.value_amount == 144 * 100.5

def test_research_entity_145_schema_validation():
    obj = ResearchSchemaEntity145Create(
        entity_code="TEST_RESEARCH_145",
        name="Test Entity 145",
        value_amount=145 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_145"
    assert obj.value_amount == 145 * 100.5

def test_research_entity_146_schema_validation():
    obj = ResearchSchemaEntity146Create(
        entity_code="TEST_RESEARCH_146",
        name="Test Entity 146",
        value_amount=146 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_146"
    assert obj.value_amount == 146 * 100.5

def test_research_entity_147_schema_validation():
    obj = ResearchSchemaEntity147Create(
        entity_code="TEST_RESEARCH_147",
        name="Test Entity 147",
        value_amount=147 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_147"
    assert obj.value_amount == 147 * 100.5

def test_research_entity_148_schema_validation():
    obj = ResearchSchemaEntity148Create(
        entity_code="TEST_RESEARCH_148",
        name="Test Entity 148",
        value_amount=148 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_148"
    assert obj.value_amount == 148 * 100.5

def test_research_entity_149_schema_validation():
    obj = ResearchSchemaEntity149Create(
        entity_code="TEST_RESEARCH_149",
        name="Test Entity 149",
        value_amount=149 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_149"
    assert obj.value_amount == 149 * 100.5

def test_research_entity_150_schema_validation():
    obj = ResearchSchemaEntity150Create(
        entity_code="TEST_RESEARCH_150",
        name="Test Entity 150",
        value_amount=150 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_150"
    assert obj.value_amount == 150 * 100.5

def test_research_entity_151_schema_validation():
    obj = ResearchSchemaEntity151Create(
        entity_code="TEST_RESEARCH_151",
        name="Test Entity 151",
        value_amount=151 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_151"
    assert obj.value_amount == 151 * 100.5

def test_research_entity_152_schema_validation():
    obj = ResearchSchemaEntity152Create(
        entity_code="TEST_RESEARCH_152",
        name="Test Entity 152",
        value_amount=152 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_152"
    assert obj.value_amount == 152 * 100.5

def test_research_entity_153_schema_validation():
    obj = ResearchSchemaEntity153Create(
        entity_code="TEST_RESEARCH_153",
        name="Test Entity 153",
        value_amount=153 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_153"
    assert obj.value_amount == 153 * 100.5

def test_research_entity_154_schema_validation():
    obj = ResearchSchemaEntity154Create(
        entity_code="TEST_RESEARCH_154",
        name="Test Entity 154",
        value_amount=154 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_154"
    assert obj.value_amount == 154 * 100.5

def test_research_entity_155_schema_validation():
    obj = ResearchSchemaEntity155Create(
        entity_code="TEST_RESEARCH_155",
        name="Test Entity 155",
        value_amount=155 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_155"
    assert obj.value_amount == 155 * 100.5

def test_research_entity_156_schema_validation():
    obj = ResearchSchemaEntity156Create(
        entity_code="TEST_RESEARCH_156",
        name="Test Entity 156",
        value_amount=156 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_156"
    assert obj.value_amount == 156 * 100.5

def test_research_entity_157_schema_validation():
    obj = ResearchSchemaEntity157Create(
        entity_code="TEST_RESEARCH_157",
        name="Test Entity 157",
        value_amount=157 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_157"
    assert obj.value_amount == 157 * 100.5

def test_research_entity_158_schema_validation():
    obj = ResearchSchemaEntity158Create(
        entity_code="TEST_RESEARCH_158",
        name="Test Entity 158",
        value_amount=158 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_158"
    assert obj.value_amount == 158 * 100.5

def test_research_entity_159_schema_validation():
    obj = ResearchSchemaEntity159Create(
        entity_code="TEST_RESEARCH_159",
        name="Test Entity 159",
        value_amount=159 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_159"
    assert obj.value_amount == 159 * 100.5

def test_research_entity_160_schema_validation():
    obj = ResearchSchemaEntity160Create(
        entity_code="TEST_RESEARCH_160",
        name="Test Entity 160",
        value_amount=160 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_160"
    assert obj.value_amount == 160 * 100.5

def test_research_entity_161_schema_validation():
    obj = ResearchSchemaEntity161Create(
        entity_code="TEST_RESEARCH_161",
        name="Test Entity 161",
        value_amount=161 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_161"
    assert obj.value_amount == 161 * 100.5

def test_research_entity_162_schema_validation():
    obj = ResearchSchemaEntity162Create(
        entity_code="TEST_RESEARCH_162",
        name="Test Entity 162",
        value_amount=162 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_162"
    assert obj.value_amount == 162 * 100.5

def test_research_entity_163_schema_validation():
    obj = ResearchSchemaEntity163Create(
        entity_code="TEST_RESEARCH_163",
        name="Test Entity 163",
        value_amount=163 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_163"
    assert obj.value_amount == 163 * 100.5

def test_research_entity_164_schema_validation():
    obj = ResearchSchemaEntity164Create(
        entity_code="TEST_RESEARCH_164",
        name="Test Entity 164",
        value_amount=164 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_164"
    assert obj.value_amount == 164 * 100.5

def test_research_entity_165_schema_validation():
    obj = ResearchSchemaEntity165Create(
        entity_code="TEST_RESEARCH_165",
        name="Test Entity 165",
        value_amount=165 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_165"
    assert obj.value_amount == 165 * 100.5

def test_research_entity_166_schema_validation():
    obj = ResearchSchemaEntity166Create(
        entity_code="TEST_RESEARCH_166",
        name="Test Entity 166",
        value_amount=166 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_166"
    assert obj.value_amount == 166 * 100.5

def test_research_entity_167_schema_validation():
    obj = ResearchSchemaEntity167Create(
        entity_code="TEST_RESEARCH_167",
        name="Test Entity 167",
        value_amount=167 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_167"
    assert obj.value_amount == 167 * 100.5

def test_research_entity_168_schema_validation():
    obj = ResearchSchemaEntity168Create(
        entity_code="TEST_RESEARCH_168",
        name="Test Entity 168",
        value_amount=168 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_168"
    assert obj.value_amount == 168 * 100.5

def test_research_entity_169_schema_validation():
    obj = ResearchSchemaEntity169Create(
        entity_code="TEST_RESEARCH_169",
        name="Test Entity 169",
        value_amount=169 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_169"
    assert obj.value_amount == 169 * 100.5

def test_research_entity_170_schema_validation():
    obj = ResearchSchemaEntity170Create(
        entity_code="TEST_RESEARCH_170",
        name="Test Entity 170",
        value_amount=170 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_170"
    assert obj.value_amount == 170 * 100.5

def test_research_entity_171_schema_validation():
    obj = ResearchSchemaEntity171Create(
        entity_code="TEST_RESEARCH_171",
        name="Test Entity 171",
        value_amount=171 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_171"
    assert obj.value_amount == 171 * 100.5

def test_research_entity_172_schema_validation():
    obj = ResearchSchemaEntity172Create(
        entity_code="TEST_RESEARCH_172",
        name="Test Entity 172",
        value_amount=172 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_172"
    assert obj.value_amount == 172 * 100.5

def test_research_entity_173_schema_validation():
    obj = ResearchSchemaEntity173Create(
        entity_code="TEST_RESEARCH_173",
        name="Test Entity 173",
        value_amount=173 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_173"
    assert obj.value_amount == 173 * 100.5

def test_research_entity_174_schema_validation():
    obj = ResearchSchemaEntity174Create(
        entity_code="TEST_RESEARCH_174",
        name="Test Entity 174",
        value_amount=174 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_174"
    assert obj.value_amount == 174 * 100.5

def test_research_entity_175_schema_validation():
    obj = ResearchSchemaEntity175Create(
        entity_code="TEST_RESEARCH_175",
        name="Test Entity 175",
        value_amount=175 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_175"
    assert obj.value_amount == 175 * 100.5

def test_research_entity_176_schema_validation():
    obj = ResearchSchemaEntity176Create(
        entity_code="TEST_RESEARCH_176",
        name="Test Entity 176",
        value_amount=176 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_176"
    assert obj.value_amount == 176 * 100.5

def test_research_entity_177_schema_validation():
    obj = ResearchSchemaEntity177Create(
        entity_code="TEST_RESEARCH_177",
        name="Test Entity 177",
        value_amount=177 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_177"
    assert obj.value_amount == 177 * 100.5

def test_research_entity_178_schema_validation():
    obj = ResearchSchemaEntity178Create(
        entity_code="TEST_RESEARCH_178",
        name="Test Entity 178",
        value_amount=178 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_178"
    assert obj.value_amount == 178 * 100.5

def test_research_entity_179_schema_validation():
    obj = ResearchSchemaEntity179Create(
        entity_code="TEST_RESEARCH_179",
        name="Test Entity 179",
        value_amount=179 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_179"
    assert obj.value_amount == 179 * 100.5

def test_research_entity_180_schema_validation():
    obj = ResearchSchemaEntity180Create(
        entity_code="TEST_RESEARCH_180",
        name="Test Entity 180",
        value_amount=180 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_180"
    assert obj.value_amount == 180 * 100.5

def test_research_entity_181_schema_validation():
    obj = ResearchSchemaEntity181Create(
        entity_code="TEST_RESEARCH_181",
        name="Test Entity 181",
        value_amount=181 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_181"
    assert obj.value_amount == 181 * 100.5

def test_research_entity_182_schema_validation():
    obj = ResearchSchemaEntity182Create(
        entity_code="TEST_RESEARCH_182",
        name="Test Entity 182",
        value_amount=182 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_182"
    assert obj.value_amount == 182 * 100.5

def test_research_entity_183_schema_validation():
    obj = ResearchSchemaEntity183Create(
        entity_code="TEST_RESEARCH_183",
        name="Test Entity 183",
        value_amount=183 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_183"
    assert obj.value_amount == 183 * 100.5

def test_research_entity_184_schema_validation():
    obj = ResearchSchemaEntity184Create(
        entity_code="TEST_RESEARCH_184",
        name="Test Entity 184",
        value_amount=184 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_184"
    assert obj.value_amount == 184 * 100.5

def test_research_entity_185_schema_validation():
    obj = ResearchSchemaEntity185Create(
        entity_code="TEST_RESEARCH_185",
        name="Test Entity 185",
        value_amount=185 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_185"
    assert obj.value_amount == 185 * 100.5

def test_research_entity_186_schema_validation():
    obj = ResearchSchemaEntity186Create(
        entity_code="TEST_RESEARCH_186",
        name="Test Entity 186",
        value_amount=186 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_186"
    assert obj.value_amount == 186 * 100.5

def test_research_entity_187_schema_validation():
    obj = ResearchSchemaEntity187Create(
        entity_code="TEST_RESEARCH_187",
        name="Test Entity 187",
        value_amount=187 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_187"
    assert obj.value_amount == 187 * 100.5

def test_research_entity_188_schema_validation():
    obj = ResearchSchemaEntity188Create(
        entity_code="TEST_RESEARCH_188",
        name="Test Entity 188",
        value_amount=188 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_188"
    assert obj.value_amount == 188 * 100.5

def test_research_entity_189_schema_validation():
    obj = ResearchSchemaEntity189Create(
        entity_code="TEST_RESEARCH_189",
        name="Test Entity 189",
        value_amount=189 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_189"
    assert obj.value_amount == 189 * 100.5

def test_research_entity_190_schema_validation():
    obj = ResearchSchemaEntity190Create(
        entity_code="TEST_RESEARCH_190",
        name="Test Entity 190",
        value_amount=190 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_190"
    assert obj.value_amount == 190 * 100.5

def test_research_entity_191_schema_validation():
    obj = ResearchSchemaEntity191Create(
        entity_code="TEST_RESEARCH_191",
        name="Test Entity 191",
        value_amount=191 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_191"
    assert obj.value_amount == 191 * 100.5

def test_research_entity_192_schema_validation():
    obj = ResearchSchemaEntity192Create(
        entity_code="TEST_RESEARCH_192",
        name="Test Entity 192",
        value_amount=192 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_192"
    assert obj.value_amount == 192 * 100.5

def test_research_entity_193_schema_validation():
    obj = ResearchSchemaEntity193Create(
        entity_code="TEST_RESEARCH_193",
        name="Test Entity 193",
        value_amount=193 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_193"
    assert obj.value_amount == 193 * 100.5

def test_research_entity_194_schema_validation():
    obj = ResearchSchemaEntity194Create(
        entity_code="TEST_RESEARCH_194",
        name="Test Entity 194",
        value_amount=194 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_194"
    assert obj.value_amount == 194 * 100.5

def test_research_entity_195_schema_validation():
    obj = ResearchSchemaEntity195Create(
        entity_code="TEST_RESEARCH_195",
        name="Test Entity 195",
        value_amount=195 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_195"
    assert obj.value_amount == 195 * 100.5

def test_research_entity_196_schema_validation():
    obj = ResearchSchemaEntity196Create(
        entity_code="TEST_RESEARCH_196",
        name="Test Entity 196",
        value_amount=196 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_196"
    assert obj.value_amount == 196 * 100.5

def test_research_entity_197_schema_validation():
    obj = ResearchSchemaEntity197Create(
        entity_code="TEST_RESEARCH_197",
        name="Test Entity 197",
        value_amount=197 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_197"
    assert obj.value_amount == 197 * 100.5

def test_research_entity_198_schema_validation():
    obj = ResearchSchemaEntity198Create(
        entity_code="TEST_RESEARCH_198",
        name="Test Entity 198",
        value_amount=198 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_198"
    assert obj.value_amount == 198 * 100.5

def test_research_entity_199_schema_validation():
    obj = ResearchSchemaEntity199Create(
        entity_code="TEST_RESEARCH_199",
        name="Test Entity 199",
        value_amount=199 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_199"
    assert obj.value_amount == 199 * 100.5

def test_research_entity_200_schema_validation():
    obj = ResearchSchemaEntity200Create(
        entity_code="TEST_RESEARCH_200",
        name="Test Entity 200",
        value_amount=200 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_200"
    assert obj.value_amount == 200 * 100.5

def test_research_entity_201_schema_validation():
    obj = ResearchSchemaEntity201Create(
        entity_code="TEST_RESEARCH_201",
        name="Test Entity 201",
        value_amount=201 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_201"
    assert obj.value_amount == 201 * 100.5

def test_research_entity_202_schema_validation():
    obj = ResearchSchemaEntity202Create(
        entity_code="TEST_RESEARCH_202",
        name="Test Entity 202",
        value_amount=202 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_202"
    assert obj.value_amount == 202 * 100.5

def test_research_entity_203_schema_validation():
    obj = ResearchSchemaEntity203Create(
        entity_code="TEST_RESEARCH_203",
        name="Test Entity 203",
        value_amount=203 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_203"
    assert obj.value_amount == 203 * 100.5

def test_research_entity_204_schema_validation():
    obj = ResearchSchemaEntity204Create(
        entity_code="TEST_RESEARCH_204",
        name="Test Entity 204",
        value_amount=204 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_204"
    assert obj.value_amount == 204 * 100.5

def test_research_entity_205_schema_validation():
    obj = ResearchSchemaEntity205Create(
        entity_code="TEST_RESEARCH_205",
        name="Test Entity 205",
        value_amount=205 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_205"
    assert obj.value_amount == 205 * 100.5

def test_research_entity_206_schema_validation():
    obj = ResearchSchemaEntity206Create(
        entity_code="TEST_RESEARCH_206",
        name="Test Entity 206",
        value_amount=206 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_206"
    assert obj.value_amount == 206 * 100.5

def test_research_entity_207_schema_validation():
    obj = ResearchSchemaEntity207Create(
        entity_code="TEST_RESEARCH_207",
        name="Test Entity 207",
        value_amount=207 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_207"
    assert obj.value_amount == 207 * 100.5

def test_research_entity_208_schema_validation():
    obj = ResearchSchemaEntity208Create(
        entity_code="TEST_RESEARCH_208",
        name="Test Entity 208",
        value_amount=208 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_208"
    assert obj.value_amount == 208 * 100.5

def test_research_entity_209_schema_validation():
    obj = ResearchSchemaEntity209Create(
        entity_code="TEST_RESEARCH_209",
        name="Test Entity 209",
        value_amount=209 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_209"
    assert obj.value_amount == 209 * 100.5

def test_research_entity_210_schema_validation():
    obj = ResearchSchemaEntity210Create(
        entity_code="TEST_RESEARCH_210",
        name="Test Entity 210",
        value_amount=210 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_210"
    assert obj.value_amount == 210 * 100.5

def test_research_entity_211_schema_validation():
    obj = ResearchSchemaEntity211Create(
        entity_code="TEST_RESEARCH_211",
        name="Test Entity 211",
        value_amount=211 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_211"
    assert obj.value_amount == 211 * 100.5

def test_research_entity_212_schema_validation():
    obj = ResearchSchemaEntity212Create(
        entity_code="TEST_RESEARCH_212",
        name="Test Entity 212",
        value_amount=212 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_212"
    assert obj.value_amount == 212 * 100.5

def test_research_entity_213_schema_validation():
    obj = ResearchSchemaEntity213Create(
        entity_code="TEST_RESEARCH_213",
        name="Test Entity 213",
        value_amount=213 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_213"
    assert obj.value_amount == 213 * 100.5

def test_research_entity_214_schema_validation():
    obj = ResearchSchemaEntity214Create(
        entity_code="TEST_RESEARCH_214",
        name="Test Entity 214",
        value_amount=214 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_214"
    assert obj.value_amount == 214 * 100.5

def test_research_entity_215_schema_validation():
    obj = ResearchSchemaEntity215Create(
        entity_code="TEST_RESEARCH_215",
        name="Test Entity 215",
        value_amount=215 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_215"
    assert obj.value_amount == 215 * 100.5

def test_research_entity_216_schema_validation():
    obj = ResearchSchemaEntity216Create(
        entity_code="TEST_RESEARCH_216",
        name="Test Entity 216",
        value_amount=216 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_216"
    assert obj.value_amount == 216 * 100.5

def test_research_entity_217_schema_validation():
    obj = ResearchSchemaEntity217Create(
        entity_code="TEST_RESEARCH_217",
        name="Test Entity 217",
        value_amount=217 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_217"
    assert obj.value_amount == 217 * 100.5

def test_research_entity_218_schema_validation():
    obj = ResearchSchemaEntity218Create(
        entity_code="TEST_RESEARCH_218",
        name="Test Entity 218",
        value_amount=218 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_218"
    assert obj.value_amount == 218 * 100.5

def test_research_entity_219_schema_validation():
    obj = ResearchSchemaEntity219Create(
        entity_code="TEST_RESEARCH_219",
        name="Test Entity 219",
        value_amount=219 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_219"
    assert obj.value_amount == 219 * 100.5

def test_research_entity_220_schema_validation():
    obj = ResearchSchemaEntity220Create(
        entity_code="TEST_RESEARCH_220",
        name="Test Entity 220",
        value_amount=220 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_220"
    assert obj.value_amount == 220 * 100.5

def test_research_entity_221_schema_validation():
    obj = ResearchSchemaEntity221Create(
        entity_code="TEST_RESEARCH_221",
        name="Test Entity 221",
        value_amount=221 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_221"
    assert obj.value_amount == 221 * 100.5

def test_research_entity_222_schema_validation():
    obj = ResearchSchemaEntity222Create(
        entity_code="TEST_RESEARCH_222",
        name="Test Entity 222",
        value_amount=222 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_222"
    assert obj.value_amount == 222 * 100.5

def test_research_entity_223_schema_validation():
    obj = ResearchSchemaEntity223Create(
        entity_code="TEST_RESEARCH_223",
        name="Test Entity 223",
        value_amount=223 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_223"
    assert obj.value_amount == 223 * 100.5

def test_research_entity_224_schema_validation():
    obj = ResearchSchemaEntity224Create(
        entity_code="TEST_RESEARCH_224",
        name="Test Entity 224",
        value_amount=224 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_224"
    assert obj.value_amount == 224 * 100.5

def test_research_entity_225_schema_validation():
    obj = ResearchSchemaEntity225Create(
        entity_code="TEST_RESEARCH_225",
        name="Test Entity 225",
        value_amount=225 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_225"
    assert obj.value_amount == 225 * 100.5

def test_research_entity_226_schema_validation():
    obj = ResearchSchemaEntity226Create(
        entity_code="TEST_RESEARCH_226",
        name="Test Entity 226",
        value_amount=226 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_226"
    assert obj.value_amount == 226 * 100.5

def test_research_entity_227_schema_validation():
    obj = ResearchSchemaEntity227Create(
        entity_code="TEST_RESEARCH_227",
        name="Test Entity 227",
        value_amount=227 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_227"
    assert obj.value_amount == 227 * 100.5

def test_research_entity_228_schema_validation():
    obj = ResearchSchemaEntity228Create(
        entity_code="TEST_RESEARCH_228",
        name="Test Entity 228",
        value_amount=228 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_228"
    assert obj.value_amount == 228 * 100.5

def test_research_entity_229_schema_validation():
    obj = ResearchSchemaEntity229Create(
        entity_code="TEST_RESEARCH_229",
        name="Test Entity 229",
        value_amount=229 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_229"
    assert obj.value_amount == 229 * 100.5

def test_research_entity_230_schema_validation():
    obj = ResearchSchemaEntity230Create(
        entity_code="TEST_RESEARCH_230",
        name="Test Entity 230",
        value_amount=230 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_230"
    assert obj.value_amount == 230 * 100.5

def test_research_entity_231_schema_validation():
    obj = ResearchSchemaEntity231Create(
        entity_code="TEST_RESEARCH_231",
        name="Test Entity 231",
        value_amount=231 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_231"
    assert obj.value_amount == 231 * 100.5

def test_research_entity_232_schema_validation():
    obj = ResearchSchemaEntity232Create(
        entity_code="TEST_RESEARCH_232",
        name="Test Entity 232",
        value_amount=232 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_232"
    assert obj.value_amount == 232 * 100.5

def test_research_entity_233_schema_validation():
    obj = ResearchSchemaEntity233Create(
        entity_code="TEST_RESEARCH_233",
        name="Test Entity 233",
        value_amount=233 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_233"
    assert obj.value_amount == 233 * 100.5

def test_research_entity_234_schema_validation():
    obj = ResearchSchemaEntity234Create(
        entity_code="TEST_RESEARCH_234",
        name="Test Entity 234",
        value_amount=234 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_234"
    assert obj.value_amount == 234 * 100.5

def test_research_entity_235_schema_validation():
    obj = ResearchSchemaEntity235Create(
        entity_code="TEST_RESEARCH_235",
        name="Test Entity 235",
        value_amount=235 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_235"
    assert obj.value_amount == 235 * 100.5

def test_research_entity_236_schema_validation():
    obj = ResearchSchemaEntity236Create(
        entity_code="TEST_RESEARCH_236",
        name="Test Entity 236",
        value_amount=236 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_236"
    assert obj.value_amount == 236 * 100.5

def test_research_entity_237_schema_validation():
    obj = ResearchSchemaEntity237Create(
        entity_code="TEST_RESEARCH_237",
        name="Test Entity 237",
        value_amount=237 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_237"
    assert obj.value_amount == 237 * 100.5

def test_research_entity_238_schema_validation():
    obj = ResearchSchemaEntity238Create(
        entity_code="TEST_RESEARCH_238",
        name="Test Entity 238",
        value_amount=238 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_238"
    assert obj.value_amount == 238 * 100.5

def test_research_entity_239_schema_validation():
    obj = ResearchSchemaEntity239Create(
        entity_code="TEST_RESEARCH_239",
        name="Test Entity 239",
        value_amount=239 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_239"
    assert obj.value_amount == 239 * 100.5

def test_research_entity_240_schema_validation():
    obj = ResearchSchemaEntity240Create(
        entity_code="TEST_RESEARCH_240",
        name="Test Entity 240",
        value_amount=240 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_240"
    assert obj.value_amount == 240 * 100.5

def test_research_entity_241_schema_validation():
    obj = ResearchSchemaEntity241Create(
        entity_code="TEST_RESEARCH_241",
        name="Test Entity 241",
        value_amount=241 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_241"
    assert obj.value_amount == 241 * 100.5

def test_research_entity_242_schema_validation():
    obj = ResearchSchemaEntity242Create(
        entity_code="TEST_RESEARCH_242",
        name="Test Entity 242",
        value_amount=242 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_242"
    assert obj.value_amount == 242 * 100.5

def test_research_entity_243_schema_validation():
    obj = ResearchSchemaEntity243Create(
        entity_code="TEST_RESEARCH_243",
        name="Test Entity 243",
        value_amount=243 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_243"
    assert obj.value_amount == 243 * 100.5

def test_research_entity_244_schema_validation():
    obj = ResearchSchemaEntity244Create(
        entity_code="TEST_RESEARCH_244",
        name="Test Entity 244",
        value_amount=244 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_244"
    assert obj.value_amount == 244 * 100.5

def test_research_entity_245_schema_validation():
    obj = ResearchSchemaEntity245Create(
        entity_code="TEST_RESEARCH_245",
        name="Test Entity 245",
        value_amount=245 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_245"
    assert obj.value_amount == 245 * 100.5

def test_research_entity_246_schema_validation():
    obj = ResearchSchemaEntity246Create(
        entity_code="TEST_RESEARCH_246",
        name="Test Entity 246",
        value_amount=246 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_246"
    assert obj.value_amount == 246 * 100.5

def test_research_entity_247_schema_validation():
    obj = ResearchSchemaEntity247Create(
        entity_code="TEST_RESEARCH_247",
        name="Test Entity 247",
        value_amount=247 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_247"
    assert obj.value_amount == 247 * 100.5

def test_research_entity_248_schema_validation():
    obj = ResearchSchemaEntity248Create(
        entity_code="TEST_RESEARCH_248",
        name="Test Entity 248",
        value_amount=248 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_248"
    assert obj.value_amount == 248 * 100.5

def test_research_entity_249_schema_validation():
    obj = ResearchSchemaEntity249Create(
        entity_code="TEST_RESEARCH_249",
        name="Test Entity 249",
        value_amount=249 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_249"
    assert obj.value_amount == 249 * 100.5

def test_research_entity_250_schema_validation():
    obj = ResearchSchemaEntity250Create(
        entity_code="TEST_RESEARCH_250",
        name="Test Entity 250",
        value_amount=250 * 100.5
    )
    assert obj.entity_code == "TEST_RESEARCH_250"
    assert obj.value_amount == 250 * 100.5


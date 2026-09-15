/**
 * Research, Grants & Lab Inventory TypeScript Types Definitions
 */

export interface IResearchCoreEntity {
  id: number;
  entity_code: string;
  name: string;
  category: string;
  description?: string;
  status: 'ACTIVE' | 'INACTIVE' | 'ARCHIVED';
  metadata_info?: Record<string, any>;
  is_deleted: boolean;
  created_at: string;
  updated_at: string;
}

export interface IResearchDetailRecord {
  id: number;
  core_entity_id: number;
  title: string;
  record_type: string;
  value_numeric: number;
  notes?: string;
  is_flagged: boolean;
  created_at: string;
}


export interface IResearchSubModule1State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule2State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule3State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule4State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule5State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule6State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule7State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule8State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule9State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule10State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule11State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule12State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule13State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule14State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule15State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule16State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule17State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule18State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IResearchSubModule19State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}

/**
 * Sports & Extracurricular Activities TypeScript Types Definitions
 */

export interface ISportsCoreEntity {
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

export interface ISportsDetailRecord {
  id: number;
  core_entity_id: number;
  title: string;
  record_type: string;
  value_numeric: number;
  notes?: string;
  is_flagged: boolean;
  created_at: string;
}


export interface ISportsSubModule1State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule2State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule3State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule4State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule5State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule6State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule7State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule8State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule9State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule10State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule11State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule12State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule13State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule14State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule15State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule16State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule17State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule18State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface ISportsSubModule19State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}

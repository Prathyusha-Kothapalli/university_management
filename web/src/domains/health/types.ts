/**
 * Campus Health & Clinic Management TypeScript Types Definitions
 */

export interface IHealthCoreEntity {
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

export interface IHealthDetailRecord {
  id: number;
  core_entity_id: number;
  title: string;
  record_type: string;
  value_numeric: number;
  notes?: string;
  is_flagged: boolean;
  created_at: string;
}


export interface IHealthSubModule1State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule2State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule3State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule4State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule5State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule6State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule7State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule8State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule9State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule10State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule11State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule12State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule13State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule14State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule15State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule16State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule17State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule18State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHealthSubModule19State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}

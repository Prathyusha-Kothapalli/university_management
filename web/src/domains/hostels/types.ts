/**
 * Student Life & Hostel Operations TypeScript Types Definitions
 */

export interface IHostelsCoreEntity {
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

export interface IHostelsDetailRecord {
  id: number;
  core_entity_id: number;
  title: string;
  record_type: string;
  value_numeric: number;
  notes?: string;
  is_flagged: boolean;
  created_at: string;
}


export interface IHostelsSubModule1State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule2State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule3State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule4State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule5State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule6State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule7State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule8State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule9State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule10State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule11State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule12State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule13State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule14State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule15State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule16State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule17State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule18State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}


export interface IHostelsSubModule19State {
  id: number;
  reference_number: string;
  label: string;
  priority: number;
  isActive: boolean;
  configuration: Record<string, any>;
  remarks?: string;
}

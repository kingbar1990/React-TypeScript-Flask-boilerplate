export interface ServerResponse {
  data: ServerData
}

export interface ServerData {
  id: string
  name?: string
  version?: string
  file?: string
  versions: []
  updateParent?: any
}

export interface Popup {
  showPopup?: any
  closePopup?: any
  updateParent?: any
  loadData?: any
  appId?: string
}
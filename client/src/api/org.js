import request from '@/utils/request'

export function getOrgAll() {
  return request({
    url: '/rbac/organization/',
    method: 'get',
  })
}
export function getOrgList(query) {
  return request({
    url: '/rbac/organization/',
    method: 'get',
    params:query
  })
}
export function createOrg(data) {
  return request({
    url: '/rbac/organization/',
    method: 'post',
    data
  })
}
export function updateOrg(id, data) {
  return request({
    url: `/rbac/organization/${id}/`,
    method: 'put',
    data
  })
}
export function deleteOrg(id) {
  return request({
    url: `/rbac/organization/${id}/`,
    method: 'delete',
  })
}
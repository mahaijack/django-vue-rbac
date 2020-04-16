import request from '@/utils/request'

export function getRoutes() {
  return request({
    url: '/rbac/permission/',
    method: 'get'
  })
}

export function getRoleAll() {
  return request({
    url: '/rbac/role/',
    method: 'get'
  })
}

export function createRole(data) {
  return request({
    url: '/rbac/role/',
    method: 'post',
    data
  })
}

export function updateRole(id, data) {
  return request({
    url: `/rbac/role/${id}/`,
    method: 'put',
    data
  })
}

export function deleteRole(id) {
  return request({
    url: `/rbac/role/${id}/`,
    method: 'delete'
  })
}

import request from '@/utils/request'


export function getPositionAll() {
  return request({
    url: '/rbac/position/',
    method: 'get'
  })
}

export function createPosition(data) {
  return request({
    url: '/rbac/position/',
    method: 'post',
    data
  })
}

export function updatePosition(id, data) {
  return request({
    url: `/rbac/position/${id}/`,
    method: 'put',
    data
  })
}

export function deletePosition(id) {
  return request({
    url: `/rbac/position/${id}/`,
    method: 'delete'
  })
}

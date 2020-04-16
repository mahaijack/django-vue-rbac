import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/token/',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/token/black/',
    method: 'get'
  })
}


export function getInfo() {
  return request({
    url: '/rbac/user/info/',
    method: 'get'
  })
}



export function getUserList(query) {
  return request({
    url: '/rbac/user/',
    method: 'get',
    params: query
  })
}

export function getUser(id) {
  return request({
    url: `/rbac/user/${id}/`,
    method: 'get'
  })
}

export function createUser(data) {
  return request({
    url: '/rbac/user/',
    method: 'post',
    data
  })
}

export function updateUser(id, data) {
  return request({
    url: `/rbac/user/${id}/`,
    method: 'put',
    data
  })
}

export function deleteUser(id, data) {
  return request({
    url: `/rbac/user/${id}/`,
    method: 'delete',
    data
  })
}

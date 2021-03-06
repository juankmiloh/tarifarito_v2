/* jshint esversion: 6 */
/* eslint-disable */
import request from '@/utils/request'

export function login(data) {
    return request({
        url: '/user/login',
        method: 'post',
        data
    })
}

export function getInfo(data) {
    return request({
        url: '/user/info',
        method: 'post',
        data
        // params: { 'token': token, 'api': process.env.VUE_APP_BASE_API }
    })
}

export function logout() {
    return request({
        url: '/user/logout',
        method: 'post'
    })
}
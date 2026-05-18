package com.example.kmp_ci_cd

interface Platform {
    val name: String
}

expect fun getPlatform(): Platform
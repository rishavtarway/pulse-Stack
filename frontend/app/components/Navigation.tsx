'use client'
import Link from 'next/link'
import { useState } from 'react'

export default function Navigation() {
  return (
    <nav className="border-b border-slate-800 bg-slate-900/50 backdrop-blur-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
        <div className="flex items-center gap-8">
          <Link href="/" className="flex items-center gap-2 group">
            <div className="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center font-black group-hover:scale-110 transition shadow-[0_0_15px_rgba(79,70,229,0.5)]">P</div>
            <span className="text-xl font-bold tracking-tight text-slate-100">Pulse<span className="text-indigo-400">Stack</span></span>
          </Link>
          <div className="hidden md:flex gap-6 text-sm font-medium text-slate-400">
            <Link href="/" className="hover:text-white transition">Insights</Link>
            <Link href="/" className="hover:text-white transition">Community</Link>
            <Link href="/" className="hover:text-white transition">Challenges</Link>
          </div>
        </div>
        <div className="flex items-center gap-4">
           <Link href="/login" className="text-sm font-semibold hover:text-indigo-400 transition">Login</Link>
           <Link href="/login" className="bg-indigo-600 hover:bg-indigo-500 px-4 py-2 rounded-lg text-sm font-bold transition">Get Started</Link>
        </div>
      </div>
    </nav>
  )
}

import Link from 'next/link'
import Navigation from './components/Navigation'
export default function Home() {
  return (
    <div className="min-h-screen bg-slate-900 text-white font-sans">
      <Navigation />
      
      <main className="max-w-7xl mx-auto px-6 py-12">
        <header className="mb-12 flex justify-between items-end">
          <div>
            <h1 className="text-4xl font-extrabold tracking-tight text-indigo-400">PulseStack Overview</h1>
            <p className="mt-2 text-slate-400">Real-time community wellness analytics and engagement.</p>
          </div>
          <Link href="/login" className="bg-indigo-600 hover:bg-indigo-500 px-6 py-3 rounded-lg font-bold transition">
            Member Login
          </Link>
        </header>
        {/* Analytics Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          {[
            { label: 'Total Steps Today', value: '1,284,592', change: '+12%', color: 'border-blue-500' },
            { label: 'Active Challenges', value: '42', change: '8 Starting Soon', color: 'border-emerald-500' },
            { label: 'Avg Pulse Engagement', value: '88%', change: 'Very High', color: 'border-indigo-500' },
          ].map((stat, i) => (
            <div key={i} className={`bg-slate-800 p-6 rounded-2xl border-l-4 ${stat.color} shadow-xl`}>
              <p className="text-slate-400 font-medium">{stat.label}</p>
              <div className="flex items-baseline gap-2 mt-2">
                <span className="text-3xl font-bold">{stat.value}</span>
                <span className="text-xs font-semibold text-emerald-400">{stat.change}</span>
              </div>
            </div>
          ))}
        </div>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Live Activity Feed */}
          <div className="bg-slate-800/50 p-8 rounded-2xl border border-slate-700 shadow-xl">
            <h2 className="text-xl font-bold mb-6 flex items-center gap-2">
              <span className="w-2 h-2 bg-red-500 rounded-full animate-pulse"></span>
              Live Pulse Feed
            </h2>
            <div className="space-y-6">
              {[
                { u: 'Rishav', a: 'Synchronized Activity Log', t: '2m ago' },
                { u: 'Sarah', a: 'Completed 10k Step Challenge', t: '5m ago' },
                { u: 'System', a: 'New Weekly Goal Generated', t: '12m ago' },
              ].map((item, i) => (
                <div key={i} className="flex justify-between items-center border-b border-slate-700 pb-4">
                  <div>
                    <span className="font-bold text-indigo-400">{item.u}</span>
                    <p className="text-sm text-slate-300">{item.a}</p>
                  </div>
                  <span className="text-xs text-slate-500">{item.t}</span>
                </div>
              ))}
            </div>
          </div>
          {/* Integration Proof Section */}
          <div className="bg-gradient-to-br from-indigo-900/40 to-slate-800 p-8 rounded-2xl border border-slate-700 shadow-xl flex flex-col justify-center">
            <h2 className="text-2xl font-bold mb-4">Engineering Capabilities</h2>
            <ul className="space-y-4 text-slate-300">
              <li className="flex gap-3">
                <span className="text-indigo-400">✔</span> Full OAuth2 JWT Authentication
              </li>
              <li className="flex gap-3">
                <span className="text-indigo-400">✔</span> MongoDB Aggregate Wellness Services
              </li>
              <li className="flex gap-3">
                <span className="text-indigo-400">✔</span> Next.js 14 Server-Side Performance
              </li>
            </ul>
          </div>
        </div>
      </main>
    </div>
  )
}

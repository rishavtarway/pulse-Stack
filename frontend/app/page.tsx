
export default function Home() {
  return (
    <div className="min-h-screen bg-[#0f172a] text-white selection:bg-indigo-500/30">
      
      {/* Hero Section */}
      <section className="relative pt-20 pb-12 overflow-hidden">
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-[500px] bg-indigo-600/10 blur-[120px] rounded-full"></div>
        
        <div className="max-w-7xl mx-auto px-6 relative">
          <div className="flex flex-col md:flex-row justify-between items-center gap-8">
            <div className="max-w-2xl">
              <span className="inline-block px-3 py-1 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-bold tracking-wider uppercase mb-4">
                Enterprise Wellness Intelligence
              </span>
              <h1 className="text-5xl md:text-6xl font-black tracking-tight leading-tight">
                Predictive Analytics <br/>
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-emerald-400">For Modern Teams</span>
              </h1>
              <p className="mt-6 text-lg text-slate-400 leading-relaxed max-w-lg">
                Unlock deeper insights into team engagement, activity trends, and burnout prevention with the PulseStack full-stack ecosystem.
              </p>
            </div>
            
            <div className="bg-slate-800/40 border border-slate-700 p-8 rounded-3xl backdrop-blur-xl shadow-2xl w-full max-w-md">
                <div className="flex justify-between items-end mb-6">
                    <h3 className="font-bold text-slate-200">System Integration</h3>
                    <span className="text-xs text-emerald-400 font-bold flex items-center gap-1">
                        <span className="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-ping"></span> Live
                    </span>
                </div>
                <div className="space-y-4">
                    <div className="h-2 w-full bg-slate-700 rounded-full overflow-hidden">
                        <div className="h-full w-3/4 bg-indigo-500"></div>
                    </div>
                    <div className="flex justify-between text-xs text-slate-400">
                        <span>Database Sync (MongoDB)</span>
                        <span>94% Accurate</span>
                    </div>
                    <div className="h-2 w-full bg-slate-700 rounded-full overflow-hidden">
                        <div className="h-full w-1/2 bg-emerald-500 animate-pulse"></div>
                    </div>
                    <div className="flex justify-between text-xs text-slate-400">
                         <span>API Latency (FastAPI)</span>
                         <span>24ms</span>
                    </div>
                </div>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <main className="max-w-7xl mx-auto px-6 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-16">
          {[
            { label: 'Active Users', value: '+1.2k', sub: 'Weekly', color: 'text-indigo-400' },
            { label: 'Avg Pulse Rate', value: '88.2', sub: 'Engagement Score', color: 'text-emerald-400' },
            { label: 'Total Challenges', value: '142', sub: 'In Progress', color: 'text-blue-400' },
            { label: 'DB Uptime', value: '99.9%', sub: 'MongoDB Atlas', color: 'text-rose-400' },
          ].map((stat, i) => (
            <div key={i} className="bg-slate-800/20 p-6 rounded-2xl border border-slate-800 hover:border-slate-700 transition group">
              <p className="text-slate-500 text-sm font-bold uppercase tracking-widest mb-2">{stat.label}</p>
              <div className={`text-4xl font-black ${stat.color} group-hover:scale-105 transition`}>{stat.value}</div>
              <p className="text-xs text-slate-600 mt-1 font-medium">{stat.sub}</p>
            </div>
          ))}
        </div>
      </main>
    </div>
  )
}

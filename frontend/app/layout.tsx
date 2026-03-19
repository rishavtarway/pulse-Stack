import './assets/css/main.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import Navigation from './components/Navigation'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'PulseStack | Enterprise Wellness Intelligence',
  description: 'Predictive analytics for modern teams and employee engagement.',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="flex flex-col min-h-screen bg-[#0f172a]">
          <Navigation />
          <main className="flex-grow">{children}</main>
        </div>
      </body>
    </html>
  )
}

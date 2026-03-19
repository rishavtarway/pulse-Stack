import './assets/css/main.css'
import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import Navigation from './components/Navigation'
import Providers from './components/Provider' // Adjusting to the common template path

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
    <html lang="en" className="dark">
      <body className={`${inter.className} bg-[#0f172a] text-white`}>
        <Providers>
          <div className="flex flex-col min-h-screen">
            <Navigation />
            <main className="flex-grow">{children}</main>
          </div>
        </Providers>
      </body>
    </html>
  )
}

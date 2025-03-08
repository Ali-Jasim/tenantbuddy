'use client';

import { ClerkProvider } from '@clerk/nextjs';
import './globals.css';
import { ThemeProvider } from '@/components/theme-provider';
import { useEffect, useState } from 'react';
import { metadata } from './metadata'; // Import metadata

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    setHydrated(true);
    console.log('Hydrated');
  });

  if (!hydrated) {
    return (
      <html lang="en">
        <body className="bg-black text-white flex items-center justify-center h-screen w-screen">
          <div>Loading...</div>
        </body>
      </html>
    );
  }

  return (
    <ClerkProvider>
      <html lang="en" suppressHydrationWarning>
        <head>
          <title>{String(metadata.title)}</title>
          <meta
            name="description"
            content={metadata.description ?? 'Default Description'}
          />
        </head>
        <body>
          <ThemeProvider
            attribute="class"
            defaultTheme="dark"
            enableSystem
            disableTransitionOnChange
          >
            {/* Render extracted content */}
            {children}
          </ThemeProvider>
        </body>
      </html>
    </ClerkProvider>
  );
}

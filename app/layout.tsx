'use client';

import { ClerkProvider, SignedIn, SignedOut } from '@clerk/nextjs';
import Auth from './Blocks/Auth';
import ControlPanel from './Blocks/ControlPanel';
import './globals.css';
import { ThemeProvider } from '@/components/theme-provider';
import { SidebarProvider } from '@/components/ui/sidebar';
import { AppSidebar } from './Blocks/app-sidebar';
import { useEffect, useState } from 'react';
import { metadata } from './metadata'; // Import metadata

export default function RootLayout() {
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    setHydrated(true);
  }, []);

  if (!hydrated) {
    return null;
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
            <SignedOut>
              <Auth />
            </SignedOut>
            <SignedIn>
              <SidebarProvider>
                <AppSidebar />
                <ControlPanel />
              </SidebarProvider>
            </SignedIn>
          </ThemeProvider>
        </body>
      </html>
    </ClerkProvider>
  );
}

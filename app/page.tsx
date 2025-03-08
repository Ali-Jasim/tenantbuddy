'use client';
import { SignedIn, SignedOut } from '@clerk/nextjs';
import Auth from './Blocks/Auth';
import ControlPanel from './Blocks/ControlPanel';
import { SidebarProvider } from '@/components/ui/sidebar';
import { AppSidebar } from './Blocks/app-sidebar';

export default function Page() {
  return (
    <>
      <SignedOut>
        <Auth />
      </SignedOut>
      <SignedIn>
        <SidebarProvider>
          <AppSidebar />
          <ControlPanel />
        </SidebarProvider>
      </SignedIn>
    </>
  );
}

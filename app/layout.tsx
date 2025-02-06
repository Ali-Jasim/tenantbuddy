import type { Metadata } from "next";
import { ClerkProvider, SignedIn, SignedOut } from "@clerk/nextjs";
import Auth from "./Blocks/Auth";
import ControlPanel from "./Blocks/ControlPanel";
import "./globals.css";
import { ThemeProvider } from "next-themes";
import { SidebarProvider } from "@/components/ui/sidebar";
import { AppSidebar } from "./Blocks/app-sidebar";

export const metadata: Metadata = {
  title: "Tenant Buddy",
  description: "Tenant Buddy, the best tenant management app",
};

export default function RootLayout() {
  return (
    <ClerkProvider>
      <html lang="en" suppressHydrationWarning>
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

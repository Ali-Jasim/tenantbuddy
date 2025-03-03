'use client';

import { Button } from '@/components/ui/button';
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuItem,
  SidebarMenuSubButton,
  SidebarSeparator,
} from '@/components/ui/sidebar';
import { UserButton, useUser, useClerk } from '@clerk/nextjs';

export function AppSidebar() {
  const { user } = useUser();
  const { signOut } = useClerk();
  const buttonStyle =
    'p-4 font-normal border-2 hover:bg-neutral-950 hover:cursor-pointer rounded-md flex flex-row items-center justify-center';

  return (
    <Sidebar>
      <SidebarHeader className="mt-5">
        <div className="flex flex-row items-center justify-center gap-5">
          <UserButton appearance={{ elements: { avatarBox: 'w-10 h-10' } }} />
          <h3 className="text-xl font-semibold">{user?.fullName}</h3>
        </div>
      </SidebarHeader>
      <SidebarSeparator />
      <SidebarHeader className="font-bold text-2xl text-center mt-5">
        🧠 Information 🧠
      </SidebarHeader>
      <SidebarContent className="flex flex-col mx-3 mt-5">
        <SidebarMenu className="w-full gap-10">
          <SidebarMenuItem className="text-lg font-medium text-center">
            🏡 Properties 🏡
            <SidebarMenuSubButton className={buttonStyle}>
              Manage Properties
            </SidebarMenuSubButton>
          </SidebarMenuItem>
          <SidebarMenuItem className="text-lg font-medium text-center">
            🤡 Tenants 🤡
            <SidebarMenuSubButton className={buttonStyle}>
              Manage Tenants
            </SidebarMenuSubButton>
          </SidebarMenuItem>
          <SidebarMenuItem className="text-lg font-medium text-center">
            🛠 Contractors 🛠
            <SidebarMenuSubButton className={buttonStyle}>
              Manage Contractors
            </SidebarMenuSubButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarContent>
      <SidebarSeparator />
      <SidebarContent className="flex flex-col mx-3 mt-1">
        <SidebarMenu className="w-full gap-5">
          <SidebarHeader className="font-bold text-2xl text-center">
            Actions <br /> ✈💥🏢🏢🔥
          </SidebarHeader>
          <SidebarMenuSubButton className={buttonStyle}>
            Resolve Issues
          </SidebarMenuSubButton>
          <SidebarMenuSubButton className={buttonStyle}>
            Manage Invoices
          </SidebarMenuSubButton>
          <SidebarMenuSubButton className={buttonStyle}>
            Manage Payments
          </SidebarMenuSubButton>
          <SidebarMenuSubButton className={buttonStyle}>
            Contact Support
          </SidebarMenuSubButton>
        </SidebarMenu>
      </SidebarContent>
      <SidebarSeparator />
      <SidebarFooter>
        <Button onClick={() => {}} className="font-semibold">
          Settings
        </Button>
        <Button
          onClick={() => signOut({ redirectUrl: '/' })}
          className="font-semibold"
        >
          Log Out
        </Button>
      </SidebarFooter>
      <SidebarGroup />
    </Sidebar>
  );
}

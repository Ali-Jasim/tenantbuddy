import { UserButton } from "@clerk/nextjs";
import ContractorList from "./Lists/ContractorList";
import IssuesList from "./Lists/IssueList";
import PropertiesList from "./Lists/PropertyList";
import TenantsList from "./Lists/TenantList";
import { SidebarTrigger } from "@/components/ui/sidebar";
import { AppSidebar } from "./app-sidebar";

const ControlPanel = () => {
  return (
    <div className="flex w-screen h-screen">
      <div className=" flex flex-col justify-center items-center h-full w-full  mx-5">
        <h1 className="text-4xl font-bold text=center mt-10">
          Tenant Buddy Control Panel
        </h1>
        <div className="flex flex-col h-full w-full gap-10 justify-center">
          <div className="grid grid-cols-3 gap-5 h-1/3">
            <div className="flex items-center justify-center ">
              <PropertiesList />
            </div>
            <div className="flex items-center justify-center">
              <TenantsList />
            </div>
            <div className="flex items-center justify-center">
              <ContractorList />
            </div>
          </div>
          <div className="flex items-center justify-center h-1/2">
            <IssuesList />
          </div>
        </div>
      </div>
    </div>
  );
};

export default ControlPanel;

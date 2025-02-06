import { UserButton } from "@clerk/nextjs";
import ContractorList from "./Lists/ContractorList";
import IssuesList from "./Lists/IssueList";
import PropertiesList from "./Lists/PropertyList";
import TenantsList from "./Lists/TenantList";
import { SidebarTrigger } from "@/components/ui/sidebar";
import { AppSidebar } from "./app-sidebar";
import ListContainer from "./Lists/ListContainer";
import { contractors, properties, tenants } from "./Lists/ListItems/dummyData";
import { TableCell, TableRow } from "@/components/ui/table";

const ControlPanel = () => {
  const contractorListItems = contractors.map((contractor) => {
    return (
      <>
        <TableCell className="text-center flex justify-center items-center">
          <p>{contractor.name}</p>
        </TableCell>
        <TableCell className="text-center flex justify-center items-center">
          <p>{contractor.work.join(", ")}</p>
        </TableCell>
        <TableCell className="text-center flex justify-center items-center">
          <p>{contractor.phone}</p>
        </TableCell>
        <TableCell className="text-center flex justify-center items-center">
          <p>{contractor.email}</p>
        </TableCell>
      </>
    );
  });

  const propertyListItems = properties.map((property) => {
    return (
      <>
        <TableCell className="text-center flex justify-center items-center">
          <p>{property.location}</p>
        </TableCell>
        <TableCell className="text-center flex justify-center items-center">
          <p>{property.tenant}</p>
        </TableCell>
      </>
    );
  });

  const tenantListItems = tenants.map((tenant) => {
    return (
      <>
        <TableCell className="text-center flex justify-center items-center">
          <p>{tenant.name}</p>
        </TableCell>
        <TableCell className="text-center flex justify-center items-center">
          <p>{tenant.address}</p>
        </TableCell>
        <TableCell className="text-center flex justify-center items-center">
          <p>{tenant.email}</p>
        </TableCell>
        <TableCell className="text-center flex justify-center items-center">
          <p>{tenant.phone}</p>
        </TableCell>
      </>
    );
  });

  return (
    <div className="flex w-screen h-screen bg-black">
      <div className=" flex flex-col justify-center items-center h-full w-full  mx-5">
        <h1 className="text-4xl font-bold text=center my-5">
          Tenant Buddy Control Panel
        </h1>
        <div className="flex flex-col h-full w-full gap-10 justify-center">
          <div className="grid grid-cols-[2fr_1fr_2fr] gap-10">
            <div className="flex items-center justify-center">
              <ListContainer
                title="Tenants"
                categories={["Name", "Address", "Email", "Phone"]}
                gridOptions="grid-cols-[0.5fr_2fr_2fr_1fr_]"
                listItems={tenantListItems}
              />
            </div>
            <div className="flex items-center justify-center ">
              <ListContainer
                title="Properties"
                categories={["Location", "Tenant"]}
                gridOptions="grid-cols-[1.5fr_0.5fr]"
                listItems={propertyListItems}
              />
            </div>
            <div className="flex items-center justify-center">
              <ListContainer
                title="Contractors"
                categories={["Name", "Work", "Phone", "Email"]}
                gridOptions="grid-cols-[1fr_1fr_1fr_2fr_]"
                listItems={contractorListItems}
              />
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

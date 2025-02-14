import IssuesList from './Lists/IssueList';
import ListContainer from './Lists/ListContainer';
import {
  contractors,
  properties,
  tenants,
  issues,
} from './Lists/ListItems/dummyData';
import { TableCell, TableRow } from '@/components/ui/table';
import { IssueItem } from './Lists/ListItems/issueItem';

const ControlPanel = () => {
  const contractorListItems = contractors.map((contractor) => {
    return (
      <>
        <TableCell className="text-center flex justify-center items-center">
          <p>{contractor.name}</p>
        </TableCell>
        <TableCell className="text-center flex justify-center items-center">
          <p>{contractor.work.join(', ')}</p>
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

  const issueListItems = issues.map((issue) => {
    function handleResolve(id: any): void {
      throw new Error('Function not implemented.');
    }

    return (
      <IssueItem
        key={issue.id}
        title={issue.title}
        location={issue.location}
        description={issue.description}
        status={issue.status}
        onResolve={() => handleResolve(issue.id)}
      />
    );
  });

  return (
    <div className="flex h-fit lg:w-screen lg:h-screen  ">
      <div className=" flex flex-col justify-center items-center h-full w-full">
        <h1 className="text-4xl font-bold text=center my-5">
          Tenant Buddy Control Panel
        </h1>
        <div className="flex flex-col h-full w-full  justify-center">
          <div className="lg:grid lg:grid-cols-[2fr_2fr] my-5 ">
            <div className=" lg:flex items-center justify-center ">
              <ListContainer
                title="🤡 Tenants 🤡"
                categories={['Name', 'Address', 'Email', 'Phone']}
                gridOptions="grid-cols-[1fr_2.5fr_2fr_1fr_]"
                listItems={tenantListItems}
              />
            </div>

            <div className="flex items-center my-5 lg:my-0 justify-center ">
              <ListContainer
                title="🛠 Contractors 🛠"
                categories={['Name', 'Work', 'Phone', 'Email']}
                gridOptions="grid-cols-[1fr_1fr_1fr_2fr_]"
                listItems={contractorListItems}
              />
            </div>
          </div>
          <div className="lg:flex items-center justify-center h-1/2 ">
            <div className="flex items-center justify-center ">
              <ListContainer
                title="🏡 Properties 🏡"
                categories={['Location', 'Tenant']}
                gridOptions="grid-cols-[1.5fr_0.5fr]"
                listItems={propertyListItems}
              />
            </div>

            <div className="flex items-center my-5 lg:mx-5 justify-center ">
              <ListContainer
                title="🏡 Issues 🏡"
                categories={['Issue', 'Location', 'Description', 'Action']}
                gridOptions="grid-cols-[0.5fr_1fr_2fr_2fr_0.5fr]"
                listItems={issueListItems}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ControlPanel;

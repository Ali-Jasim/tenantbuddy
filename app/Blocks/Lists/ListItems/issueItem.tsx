import { Button } from '@/components/ui/button';
import { Table, TableCell } from '@/components/ui/table';

interface IssueItemProps {
  title: string;
  location: string;
  description: string;
  status: string;
  onResolve: () => void;
}

export function IssueItem({
  title,
  location,
  description,
  status,
  onResolve,
}: IssueItemProps) {
  return (
    <>
      <TableCell className="text-center flex justify-center items-center">
        <p>{title}</p>
      </TableCell>
      <TableCell className="text-center flex justify-center items-center">
        <p>{location}</p>
      </TableCell>
      <TableCell className="text-center flex justify-center items-center">
        <p>{description}</p>
      </TableCell>
      <TableCell className="text-center flex justify-center items-center">
        <p>{status}</p>
      </TableCell>
      <TableCell className="text-center flex justify-center items-center">
        <Button
          onClick={onResolve}
          className="bg-green-500 hover:bg-green-600 font-semibold"
        >
          Resolve
        </Button>
      </TableCell>
    </>
  );
}

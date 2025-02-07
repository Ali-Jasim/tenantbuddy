import { Button } from '@/components/ui/button';
import { Card, CardHeader, CardTitle, CardFooter } from '@/components/ui/card';
import { Table, TableCell, TableHeader } from '@/components/ui/table';

export default function ListContainer({
  title,
  categories,
  gridOptions,
  button = false,
  listItems = null,
}: {
  title: string;
  categories: string[];
  gridOptions: string;
  button?: boolean;
  listItems: React.ReactNode;
}) {
  const cellCategory = renderCells();

  return (
    <Card className="w-full h-full">
      <CardHeader className="flex justify-center items-center">
        <CardTitle className="text-xl">{title}</CardTitle>
      </CardHeader>
      <div className="flex flex-col justify-center items-center border-2 m-2 rounded-md bg-neutral-950">
        <Table>
          <TableHeader className={'grid ' + gridOptions}>
            {cellCategory}
          </TableHeader>
        </Table>
      </div>
      <div className="border-2 rounded-md flex justify-between items-center mx-2 h-auto">
        <Table className={'grid ' + gridOptions}>
          {listItems || <p>no items</p>}
        </Table>
      </div>
      <CardFooter className="flex justify-center items-center h-1/5 mt-5">
        <Button className="font-bold">Manage</Button>
      </CardFooter>
    </Card>
  );

  function renderCells() {
    return categories.map((category) => {
      return (
        <TableCell key={category} className="text-center">
          <h2 className="font-semibold">{category}</h2>
        </TableCell>
      );
    });
  }
}

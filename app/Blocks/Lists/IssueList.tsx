import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import {
  Table,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

export default function IssueList() {
  return (
    <Card className="w-4/5 h-fit">
      <CardHeader className="flex justify-center items-center">
        <CardTitle className="text-xl">Issues</CardTitle>
      </CardHeader>
      <div className="flex flex-col justify-center items-center border-2 m-2 rounded-md  bg-neutral-950">
        <Table>
          <TableHeader className="grid grid-cols-[0.5fr_1fr_2fr_2fr_0.5fr]  ">
            <TableCell className="text-center">
              <h2 className="font-semibold">Issue</h2>
            </TableCell>
            <TableCell className="text-center">
              <h2 className="font-semibold">Location</h2>
            </TableCell>
            <TableCell className="text-center">
              <h2 className="font-semibold">Description</h2>
            </TableCell>
            <TableCell className="text-center">
              <h2 className="font-semibold">Action</h2>
            </TableCell>
          </TableHeader>
        </Table>
      </div>
      <div className="border-2 rounded-md flex justify-between items-center mx-2">
        <Table className="grid grid-cols-[0.5fr_1fr_2fr_2fr_0.5fr]  ">
          <TableCell className="text-center flex justify-center items-center">
            <p>Plumbing</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <p>420 Main street, Toronto</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <p>Toilet Broken</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <p>Call Plumber</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <Button className="bg-green-500 font-semibold">Resolve</Button>
          </TableCell>
        </Table>
      </div>
      <div className="border-2 rounded-md flex justify-between items-center mx-2">
        <Table className="grid grid-cols-[0.5fr_1fr_2fr_2fr_0.5fr]  ">
          <TableCell className="text-center flex justify-center items-center">
            <p>Plumbing</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <p>420 Main street, Toronto</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <p>Toilet Broken</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <p>Call Plumber</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <Button className="bg-green-500 font-semibold">Resolve</Button>
          </TableCell>
        </Table>
      </div>
      <div className="border-2 rounded-md flex justify-between items-center mx-2">
        <Table className="grid grid-cols-[0.5fr_1fr_2fr_2fr_0.5fr]  ">
          <TableCell className="text-center flex justify-center items-center">
            <p>Plumbing</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <p>420 Main street, Toronto</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <p>Toilet Broken</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <p>Call Plumber</p>
          </TableCell>
          <TableCell className="text-center flex justify-center items-center">
            <Button className="bg-green-500 font-semibold">Resolve</Button>
          </TableCell>
        </Table>
      </div>

      <CardFooter className="flex justify-center items-center h-1/5 mt-2 ">
        <Button className="font-bold">Manage</Button>
      </CardFooter>
    </Card>
  );
}

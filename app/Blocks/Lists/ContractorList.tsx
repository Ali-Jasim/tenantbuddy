import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

const ContractorList = () => {
  return (
    <Card className="w-full h-full">
      <CardHeader className="flex ">
        <CardTitle className="">Contractors</CardTitle>
        <CardDescription className="">A list of contractors</CardDescription>
      </CardHeader>
      <CardContent className="grid ">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className=""></TableHead>
              <TableHead className="">Name</TableHead>
              <TableHead className="">Specialization</TableHead>
              <TableHead className="">Location</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <TableRow>
              <TableHead className="">
                <input type="checkbox" />
              </TableHead>
              <TableCell className="">1</TableCell>
              <TableCell className="">2</TableCell>
              <TableCell className="">3</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </CardContent>
      <CardFooter className="flex justify-end ">
        <div className="flex gap-3">
          <Button className="bg-green-500">Add</Button>
          <Button className="bg-red-500">Delete</Button>
        </div>
      </CardFooter>
    </Card>
  );
};

export default ContractorList;

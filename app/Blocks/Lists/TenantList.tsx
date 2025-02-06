import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table";

export default function TenantList() {
  return (
    <Card className="w-full h-full">
      <CardHeader className="flex ">
        <CardTitle className="">Tenants</CardTitle>
        <CardDescription className="">List of tenants</CardDescription>
      </CardHeader>
      <CardContent className="grid ">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead className=""></TableHead>
              <TableHead className="">Name</TableHead>
              <TableHead className="">Phone Number</TableHead>
              <TableHead className="">Email</TableHead>
              <TableHead className="">Address</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            <TableRow>
              <TableHead className="">
                <input type="checkbox" />
              </TableHead>
              <TableCell className="">1</TableCell>
              <TableCell className="">2</TableCell>
              <TableCell className="">4</TableCell>
              <TableCell className="">5</TableCell>
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
}

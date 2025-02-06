import { Button } from "@/components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
  CardFooter,
} from "@/components/ui/card";

export default function IssueList() {
  return (
    <Card className="w-full h-full ">
      <CardHeader>
        <CardTitle>Issues</CardTitle>
        <CardDescription>A list of issues</CardDescription>
      </CardHeader>
      <CardContent className="border-2 m-2 rounded-md flex flex-col justify-start items-center h-2/3 pt-5">
        <div className="border-2 rounded-md flex justify-between items-center w-full px-5 py-1">
          <p>Card Content</p>
          <Button className="bg-green-500 font-semibold white">Resolve</Button>
        </div>
      </CardContent>
    </Card>
  );
}

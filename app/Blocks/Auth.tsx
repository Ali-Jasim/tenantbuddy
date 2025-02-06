import { SignInButton, SignUpButton } from "@clerk/nextjs";

const auth = () => {
  return (
    <body className={"flex flex-col h-screen items-center justify-center"}>
      <h1 className="text-4xl font-bold mb-20">Tenant Buddy</h1>
      <div className="flex justify-between w-1/5">
        <SignInButton className="btn btn-secondary" />
        <SignUpButton className="btn btn-secondary" />
      </div>
    </body>
  );
};

export default auth;

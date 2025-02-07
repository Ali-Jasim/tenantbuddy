// dummyData.tsx

export const landlords = [
  {
    name: "Alice Johnson",
    email: "alice.johnson@example.com",
    username: "alicejohnson",
  },
];

export const properties = [
  {
    location: "111 Sunset Blvd, Los Angeles, CA 90028",
    tenant: "Olivia Davis", // Only the tenant name is included
  },
  {
    location: "222 Bay Street, San Francisco, CA 94133",
    tenant: "Michael Brown",
  },
  {
    location: "333 Ocean Drive, Miami, FL 33139",
    tenant: "David Miller",
  },
];

export const tenants = [
  {
    name: "Olivia Davis",
    email: "olivia.davis@example.com",
    username: "oliviadavis",
    address: "123 Elm Street, Springfield, IL 62704",
    phone: "555-012-3456", // Random phone number
  },
  {
    name: "Michael Brown",
    email: "michael.brown@example.com",
    username: "michaelbrown",
    address: "456 Oak Avenue, Rivertown, CA 90210",
    phone: "555-987-6543", // Random phone number
  },
  {
    name: "David Miller",
    email: "david.miller@example.com",
    username: "davidmiller",
    address: "789 Pine Road, Denver, CO 80203",
    phone: "555-654-3210", // Random phone number
  },
];

export const contractors = [
  {
    name: "John Doe Contractors",
    work: ["Electrical", "Plumbing"],
    phone: "555-123-4567",
    email: "john.doe@contractors.com",
    location: "789 Maple Road, New York, NY 10001",
  },
  {
    name: "BuildIt Inc.",
    work: ["Masonry", "Roofing"],
    phone: "555-987-6543",
    email: "contact@buildit.com",
    location: "321 Cedar Street, Chicago, IL 60605",
  },

  {
    name: "Buildme Inc.",
    work: ["Roofing"],
    phone: "555-987-6543",
    email: "contact@buildme.com",
    location: "123 Cedar Street, Toronto, IL 60605",
  },
];

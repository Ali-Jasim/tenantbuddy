'use client';
import React, { useEffect, useState } from 'react';
import Modal from './Modal';
import axios from 'axios';

interface Tenant {
  _id: string;
  name: string;
  phone: string;
}

const HomePage: React.FC = () => {
  const [tenants, setTenants] = useState<Tenant[]>([]);

  useEffect(() => {
    const fetchTenants = async () => {
      try {
        const response = await axios.get('http://localhost:8000/tenants');
        setTenants(response.data.tenants);
      } catch (error) {
        console.error('Failed to fetch tenants:', error);
      }
    };
    fetchTenants();
  }, []);

  return (
    <div className="p-6 bg-gray-900 text-white min-h-screen">
      <h1 className="text-4xl font-bold mb-8">Landlord Dashboard</h1>

      <section className="mb-6">
        <h2 className="text-2xl font-semibold mb-4">Tenants</h2>
        <Modal name="Tenant" fields={['name', 'phone']} endpoint="/tenants" />
        <ul className="mt-4 space-y-2">
          {tenants.map((tenant) => (
            <li key={tenant._id}>
              {tenant.name} - {tenant.phone} (ID: {tenant._id})
            </li>
          ))}
        </ul>
      </section>

      <section className="mb-6">
        <h2 className="text-2xl font-semibold mb-4">Contractors</h2>
        <Modal
          name="Contractor"
          fields={['name', 'phone', 'specialty']}
          endpoint="/contractors"
        />
      </section>

      <section className="mb-6">
        <h2 className="text-2xl font-semibold mb-4">Properties</h2>
        <Modal name="Property" fields={['address']} endpoint="/properties" />
      </section>

      <section className="mb-6">
        <h2 className="text-2xl font-semibold mb-4">Issues</h2>
        <Modal
          name="Issue"
          fields={['description', 'tenantPhone']}
          endpoint="/issues"
        />
      </section>
    </div>
  );
};

export default HomePage;

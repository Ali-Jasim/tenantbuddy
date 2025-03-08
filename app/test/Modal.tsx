'use client';
import React, { useState } from 'react';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogFooter,
} from '@/components/ui/dialog';
import { Label } from '@/components/ui/label';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import axios from 'axios';

interface ModalProps {
  fields: string[];
  name: string;
  endpoint: string;
}

const Modal: React.FC<ModalProps> = ({ fields, name, endpoint }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [formData, setFormData] = useState<Record<string, string>>(
    fields.reduce((acc, field) => ({ ...acc, [field]: '' }), {})
  );

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.id]: e.target.value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const payload = new FormData();
    Object.entries(formData).forEach(([key, value]) => {
      payload.append(key, value);
    });

    try {
      await axios.post(`http://localhost:8000${endpoint}`, payload, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setIsOpen(false);
    } catch (error) {
      console.error('Failed to submit form:', error);
      alert('Error saving data. Check the console for details.');
    }
  };

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button variant="outline">Manage {name}</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>{name}</DialogTitle>
        </DialogHeader>
        <form onSubmit={handleSubmit}>
          <div className="grid gap-4 py-4">
            {fields.map((field) => (
              <div key={field} className="grid grid-cols-4 items-center gap-4">
                <Label htmlFor={field} className="text-right">
                  {field}
                </Label>
                <Input
                  id={field}
                  className="col-span-3"
                  value={formData[field]}
                  onChange={handleInputChange}
                />
              </div>
            ))}
          </div>
          <DialogFooter>
            <Button type="submit">Save Changes</Button>
          </DialogFooter>
        </form>
      </DialogContent>
    </Dialog>
  );
};

export default Modal;

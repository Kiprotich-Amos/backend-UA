"use client";
import React, { useState } from "react";
import styles from "@/app/utils/css/admin/OperationTableList.module.css"; // All CSS will be in this file

interface OperationTableFormData {
  company_user: number | null;
  name_operation: string;
  company: number | null;
  price_set: number | null;
}

const CreateOperationTableForm: React.FC = () => {
  const [formData, setFormData] = useState<OperationTableFormData>({
    company_user: null,
    name_operation: "",
    company: null,
    price_set: null,
  });

  const handleChange = (event: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    // You will implement your API submission logic here later
    console.log("Form Data:", formData);
  };

  return (
    <div className={styles["create-operation-table-form-container"]}>
      <h2>Create New Operation Table Entry</h2>
      <form onSubmit={handleSubmit} className={styles["form"]}>
        <div className={styles["form-group"]}>
          <label htmlFor="company_user">Company User:</label>
          <select
            id="company_user"
            name="company_user"
            value={formData.company_user || ""}
            onChange={handleChange}
            required
          >
            <option value="">Select Company User</option>
            {/* Placeholder options - replace with actual data later */}
            <option value="1">User A</option>
            <option value="2">User B</option>
          </select>
        </div>

        <div className={styles["form-group"]}>
          <label htmlFor="name_operation">Operation Name:</label>
          <input
            type="text"
            id="name_operation"
            name="name_operation"
            value={formData.name_operation}
            onChange={handleChange}
            required
          />
        </div>

        <div className={styles["form-group"]}>
          <label htmlFor="company">Company:</label>
          <select
            id="company"
            name="company"
            value={formData.company || ""}
            onChange={handleChange}
            required
          >
            <option value="">Select Company</option>
            {/* Placeholder options - replace with actual data later */}
            <option value="101">Company X</option>
            <option value="102">Company Y</option>
          </select>
        </div>

        <div className={styles["form-group"]}>
          <label htmlFor="price_set">Price Set:</label>
          <select
            id="price_set"
            name="price_set"
            value={formData.price_set || ""}
            onChange={handleChange}
            required
          >
            <option value="">Select Price Set</option>
            {/* Placeholder options - replace with actual data later */}
            <option value="201">Price Set Alpha</option>
            <option value="202">Price Set Beta</option>
          </select>
        </div>

        <button type="submit" className={styles["submit-button"]}>
          Create Operation
        </button>
      </form>
    </div>
  );
};

interface OperationTableData {
  id: number;
  company_user: number;
  name_operation: string;
  company: number;
  price_set: number;
}

const OperationTableList: React.FC = () => {
  // Placeholder data for demonstration
  const operations: OperationTableData[] = [
    { id: 1, company_user: 101, name_operation: "Loading", company: 201, price_set: 301 },
    { id: 2, company_user: 102, name_operation: "Unloading", company: 202, price_set: 302 },
    { id: 3, company_user: 101, name_operation: "Storage", company: 203, price_set: 303 },
    { id: 4, company_user: 103, name_operation: "Packing", company: 201, price_set: 304 },
  ];

  return (
    <div className={styles["operation-table-container"]}>
      <h2>Operation Table</h2>
      <table className={styles["operation-table"]}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Company User ID</th>
            <th>Operation Name</th>
            <th>Company ID</th>
            <th>Price Set ID</th>
          </tr>
        </thead>
        <tbody>
          {operations.map((operation) => (
            <tr key={operation.id} className={styles["operation-table-row"]}>
              <td>{operation.id}</td>
              <td>{operation.company_user}</td>
              <td>{operation.name_operation}</td>
              <td>{operation.company}</td>
              <td>{operation.price_set}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

// Combined component to render both form and table on the same page
const OperationsPage: React.FC = () => {
  return (
    <div>
      <CreateOperationTableForm />
      <OperationTableList />
    </div>
  );
};

export default OperationsPage;
"use client";
import React, { useState, ChangeEvent, FormEvent } from "react";
import styles from "@/app/utils/css/admin/contractForm.module.css";

interface ContractFormData {
  contract_name: string;
  contract_client: string; // Assuming you'll use an ID or similar
  contract_duration: string;
  expected_cargo: string;
  contract_unit_price: number | null;
  contract_start: string; // Date will be a string in the form
}

const initialFormData: ContractFormData = {
  contract_name: "",
  contract_client: "",
  contract_duration: "",
  expected_cargo: "",
  contract_unit_price: null,
  contract_start: "",
};

const ContractForm = () => {
  const [formData, setFormData] = useState<ContractFormData>(initialFormData);
  // In a real application, you would fetch this data from an API
  const [clients, setClients] = useState([
    { id: "company_id_1", name: "Company A" },
    { id: "company_id_2", name: "Company B" },
    // Add more clients here
  ]);

  const handleInputChange = (
    event: ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    const { name, value } = event.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleNumberInputChange = (
    event: ChangeEvent<HTMLInputElement>
  ) => {
    const { name, value } = event.target;
    setFormData({
      ...formData,
      [name]: value === "" ? null : parseFloat(value),
    });
  };

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    console.log("Form Data:", formData);

    // In a real application, you would send this data to your backend API
    try {
      // const response = await fetch('/api/contracts', {
      //   method: 'POST',
      //   headers: {
      //     'Content-Type': 'application/json',
      //   },
      //   body: JSON.stringify(formData),
      // });

      // if (response.ok) {
      //   console.log('Contract created successfully!');
      //   setFormData(initialFormData); // Reset the form
      // } else {
      //   console.error('Failed to create contract');
      // }
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className={styles.form}>
      <div>
        <label htmlFor="contract_name">Contract Name:</label>
        <input
          type="text"
          id="contract_name"
          name="contract_name"
          value={formData.contract_name}
          onChange={handleInputChange}
          required
        />
      </div>

      <div>
        <label htmlFor="contract_client">Client:</label>
        <select
          id="contract_client"
          name="contract_client"
          value={formData.contract_client}
          onChange={handleInputChange}
          required
          className={styles.form}
        >
          <option value="">Select Client</option>
          {clients.map((client) => (
            <option key={client.id} value={client.id}>
              {client.name}
            </option>
          ))}
        </select>
      </div>

      <div>
        <label htmlFor="contract_duration">Contract Duration:</label>
        <input
          type="text"
          id="contract_duration"
          name="contract_duration"
          value={formData.contract_duration}
          onChange={handleInputChange}
          placeholder="e.g., 1 year, 6 months"
          required
        />
      </div>

      <div>
        <label htmlFor="expected_cargo">Expected Cargo:</label>
        <textarea
          id="expected_cargo"
          name="expected_cargo"
          value={formData.expected_cargo}
          onChange={handleInputChange}
          rows={4}
          required
          className={styles.form}
        />
      </div>

      <div>
        <label htmlFor="contract_unit_price">Unit Price:</label>
        <input
          type="number"
          id="contract_unit_price"
          name="contract_unit_price"
          value={formData.contract_unit_price === null ? "" : formData.contract_unit_price}
          onChange={handleNumberInputChange}
          step="0.01"
          required
        />
      </div>

      <div>
        <label htmlFor="contract_start">Start Date:</label>
        <input
          type="date"
          id="contract_start"
          name="contract_start"
          value={formData.contract_start}
          onChange={handleInputChange}
          required
        />
      </div>

      <button type="submit" className={styles.form}>
        Save Contract
      </button>
    </form>
  );
};

export default ContractForm;
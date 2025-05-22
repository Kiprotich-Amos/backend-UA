"use client";
import React, { useState } from "react";
import styles from '@/app/utils/css/dash/consignment.module.css'; // Assuming you have some dashboard styles

interface ConsignmentInventoryFormProps {
  // You might want to pass a function here to handle form submission
  onSave?: (data: ConsignmentInventoryData) => void;
}

interface ConsignmentInventoryData {
  consignment_no: string;
  delivery_no: string;
  company_user: string; // Or a specific type for CompanyUser if needed
  company: string; // Or a specific type for Company if needed
  received_at?: Date | null;
}

const ConsignmentInventoryForm: React.FC<ConsignmentInventoryFormProps> = ({ onSave }) => {
  const [consignmentNo, setConsignmentNo] = useState("");
  const [deliveryNo, setDeliveryNo] = useState("");
  const [companyUser, setCompanyUser] = useState(""); // You might need a dropdown or input for this
  const [company, setCompany] = useState(""); // You might need a dropdown or input for this
  const [receivedAt, setReceivedAt] = useState<Date | null>(null);

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    const formData: ConsignmentInventoryData = {
      consignment_no: consignmentNo,
      delivery_no: deliveryNo,
      company_user: companyUser,
      company: company,
      received_at: receivedAt,
    };
    onSave?.(formData);
    // Optionally clear the form after submission
    setConsignmentNo("");
    setDeliveryNo("");
    setCompanyUser("");
    setCompany("");
    setReceivedAt(null);
  };

  return (
    <div className={styles.formContainer}> {/* You might need to create this style */}
      <h2>Receive Consignment</h2>
      <form onSubmit={handleSubmit}>
        <div className={styles.formGroup}>
          <label htmlFor="consignment_no">Consignment No:</label>
          <input
            type="text"
            id="consignment_no"
            value={consignmentNo}
            onChange={(e) => setConsignmentNo(e.target.value)}
            required
          />
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="delivery_no">Delivery No:</label>
          <input
            type="text"
            id="delivery_no"
            value={deliveryNo}
            onChange={(e) => setDeliveryNo(e.target.value)}
            required
          />
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="company_user">Company User:</label>
          <input
            type="text"
            id="company_user"
            value={companyUser}
            onChange={(e) => setCompanyUser(e.target.value)}
            required
          />
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="company">Company:</label>
          <input
            type="text"
            id="company"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            required
          />
        </div>

        <div className={styles.formGroup}>
          <label htmlFor="received_at">Received At:</label>
          <input
            type="datetime-local"
            id="received_at"
            value={receivedAt ? receivedAt.toISOString().slice(0, 16) : ""}
            onChange={(e) => setReceivedAt(e.target.value ? new Date(e.target.value) : null)}
          />
          <small>Leave blank if not received yet.</small>
        </div>

        <button type="submit" className={styles.submitButton}>Save Consignment</button>
      </form>
    </div>
  );
};

export default ConsignmentInventoryForm;
import React from "react";
import Input from "@/app/components/Input";
import Button from "@/app/components/Button";
import styles from "@/app/utils/css/dash/release.module.css"; // Assuming a new CSS module

const CargoItemReleaseForm = () => {
  return (
    <div className={styles.container}>
      <section className={styles.releaseCard}>
        <div className={styles.columnPair}>
          <div>
            <label htmlFor="general_cargo"> General Cargo </label>
            {/* In a real application, you would fetch existing GeneralCargo items */}
            <select id="general_cargo" name="general_cargo">
              <option value="">Select Consignment</option>
              <option value="cargo_id_1">Consignment No. ABC123</option>
              <option value="cargo_id_2">Consignment No. XYZ456</option>
              {/* Add more options as needed */}
            </select>
          </div>
          <div>
            <label htmlFor="company_user"> Company User </label>
            {/* Fetch and populate company users */}
            <select id="company_user" name="company_user">
              <option value="">Select User</option>
              <option value="user_id_1">User P</option>
              <option value="user_id_2">User Q</option>
              {/* Add more options as needed */}
            </select>
          </div>
        </div>
        <div className={styles.columnPair}>
          <div>
            <label htmlFor="transporter"> Transporter (Optional) </label>
            <Input type="text" id="transporter" name="transporter" />
          </div>
          <div>
            <label htmlFor="no_bags"> Number of Bags </label>
            <Input type="number" id="no_bags" name="no_bags" />
          </div>
        </div>
        <div className={styles.fullWidthInput}>
          <label htmlFor="net_weight"> Net Weight </label>
          <Input type="number" step="0.01" id="net_weight" name="net_weight" />
        </div>
        <div className={styles.fullWidthInput}>
          <label htmlFor="gross_weight"> Gross Weight </label>
          <Input type="number" step="0.01" id="gross_weight" name="gross_weight" />
        </div>
        <div className={styles.fullWidthInput}>
          <label htmlFor="status"> Status </label>
          <Input type="text" id="status" name="status" />
        </div>
        <div className={styles.fullWidthButton}>
          <Button type="submit">Release Cargo</Button>
        </div>
      </section>
    </div>
  );
};

export default CargoItemReleaseForm;
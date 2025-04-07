import React from "react";
import Input from "@/app/components/Input";
import Button from "@/app/components/Button";
import styles from "@/app/utils/css/dash/cargo.module.css";

const GeneralCargoForm = () => {
  return (
    <div className={styles.container}>
      <section className={styles.receivingCard}>
        <div className={styles.formColumn}>
          <div>
            <label htmlFor="consignment_no"> Consignment No </label>
            <Input type="text" id="consignment_no" name="consignment_no" />
          </div>
          <div>
            <label htmlFor="kra_no"> KRA No </label>
            <Input type="text" id="kra_no" name="kra_no" />
          </div>
          <div>
            <label htmlFor="company"> Company </label>
            <select id="company" name="company">
              <option value="">Select Company</option>
              <option value="company_id_1">Company A</option>
              <option value="company_id_2">Company B</option>
            </select>
          </div>
          <div>
            <label htmlFor="company_user"> Company User </label>
            <select id="company_user" name="company_user">
              <option value="">Select User</option>
              <option value="user_id_1">User X</option>
              <option value="user_id_2">User Y</option>
            </select>
          </div>
          <div>
            <label htmlFor="transporter"> Transporter (Optional) </label>
            <Input type="text" id="transporter" name="transporter" />
          </div>
        </div>
        <div className={styles.formColumn}>
          <div>
            <label htmlFor="no_bags"> Number of Bags </label>
            <Input type="number" id="no_bags" name="no_bags" />
          </div>
          <div>
            <label htmlFor="units_measure"> Units of Measure </label>
            <Input type="text" id="units_measure" name="units_measure" />
          </div>
          <div>
            <label htmlFor="net_weight"> Net Weight </label>
            <Input type="number" step="0.01" id="net_weight" name="net_weight" />
          </div>
          <div>
            <label htmlFor="gross_weight"> Gross Weight </label>
            <Input type="number" step="0.01" id="gross_weight" name="gross_weight" />
          </div>
          <div>
            <label htmlFor="status_one"> Status </label>
            <Input type="text" id="status_one" name="status_one" />
          </div>
        </div>
        <div className={styles.buttonContainer}>
          <Button id="submit" type="submit">Submit</Button>
        </div>
      </section>
    </div>
  );
};

export default GeneralCargoForm;
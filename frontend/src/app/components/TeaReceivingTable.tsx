import React from "react";
import styles from "./css/tea.module.css"; 
interface TeaReceivingTableProps {}

const TeaReceivingTable: React.FC<TeaReceivingTableProps> = () => {
  return (
    <section className={styles.table_card}>
      <table>
        <tbody>
          <tr>
            <td colSpan={9} className={styles["search-filter-row"]}>
              <div className={styles["search-filter-container"]}>
                <div>
                  <label htmlFor="teaSearch" className={styles["search-label"]}>
                    Tea receiving
                  </label>
                  <div className={styles["search-input-group"]}>
                    <input
                      id="teaSearch"
                      defaultValue="Search by Consignment Number"
                      type="text"
                      className={styles["search-input"]}
                    />
                    <button className={styles["search-button"]}>
                      Search
                    </button>
                    <button
                      type="button"
                      id="printSummary"
                      className={styles["print-button"]}
                    >
                      Print Summary
                    </button>
                  </div>
                </div>
                <div>
                  <label
                    htmlFor="invoiceFilter"
                    className={styles["search-label"]}
                  >
                    Filter by Invoice:
                  </label>
                  <input
                    type="text"
                    id="invoiceFilter"
                    placeholder="Invoice No."
                    className={styles["filter-input"]}
                  />
                  <button  className={styles["search-button"]}>
                    Search
                  </button>
                </div>
              </div>
            </td>
          </tr>
          <tr>
            <th>INVOICE NO</th>
            <th>GRADE</th>
            <th>GARDEN</th>
            <th>NO OF BAGS</th>
            <th>PALLET WEIGHT</th>
            <th>TARE WEIGHT</th>
            <th>NET WEIGHT</th>
            <th>GROSS WEIGHT</th>
            <th>READ WEIGH WEIGHT</th>
          </tr>
          <tr>
            <td>INV-001</td>
            <td>BP1</td>
            <td>ABC Tea Garden</td>
            <td>100</td>
            <td>50 kg</td>
            <td>5 kg</td>
            <td>45 kg</td>
            <td>55 kg</td>
            <td>
              <button className={styles["read-button"]}>Read</button>
            </td>
          </tr>
          <tr>
            <td>INV-002</td>
            <td>PF1</td>
            <td>XYZ Tea Garden</td>
            <td>120</td>
            <td>60 kg</td>
            <td>6 kg</td>
            <td>54 kg</td>
            <td>66 kg</td>
            <td>
              <button className={styles["read-button"]}>Read</button>
            </td>
          </tr>
          <tr>
            <td colSpan={9} className={styles["pagination-row"]}>
              <div className={styles["pagination-container"]}>
                <button
                  id="prevPage"
                  className={styles["pagination-button"]}
                  disabled
                >
                  Previous
                </button>
                <span id="currentPage" className={styles["current-page"]}>
                  Page 1
                </span>
                <button id="nextPage" className={styles["pagination-button"]}>
                  Next
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </section>
  );
};

export default TeaReceivingTable;